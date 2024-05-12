<template>
  <div class="navbar bg-base-300">
    <div class="flex-none">
      <label for="my-drawer-2">
        <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24"
          class="inline-block w-6 h-6 stroke-current">
          <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 6h16M4 12h16M4 18h16"></path>
        </svg>
      </label>
    </div>
    <div class="flex-1">
      <a class="btn btn-ghost text-xl">Job AI Match</a>
    </div>
    <div class="flex-none">
    </div>
  </div>
  <div class="drawer lg:drawer-open">
    <input id="my-drawer-2" type="checkbox" class="drawer-toggle" />
    <div class="drawer-content bg-base">
      <div class="flex flex-col items-start justify-between sm:flex-row">
        <div class="flex-grow mr-2">
          <div class="mx-2 font-semibold">
            <h4>Utilize o Job AI Match em 3 passos simples:</h4>
            <ol>
              <li class="my-3">
                <h2>1.Envie seu currículo:</h2>
                <ul>
                  <li>Clique no botão "ESCOLHER ARQUIVO".</li>
                  <li>Selecione o arquivo PDF do seu currículo em seu computador e faça o upload.</li>
                </ul>
              </li>
              <li class="mb-3">
                <h2>2.Cole o link da vaga:</h2>
                <ul>
                  <li>Copie o link da vaga desejada no LinkedIn, Gupy, ou outra plataforma de emprego.</li>
                  <li>Cole o link no campo designado "Link da Vaga".</li>
                  <li>Assim que terminar uma análise vc pode inserir um novo link</li>
                </ul>
              </li>
              <li class="mb-3">
                <h2>3.Aguarde o resultado:</h2>
                <ul>
                  <li>Clique no botão "Match!".</li>
                  <li>Aguarde a análise da compatibilidade.</li>
                  <li>O processo leva em média 30 segundos.</li>
                </ul>
              </li>
            </ol>

            <p class="mb-3">Pronto! Agora você tem uma análise personalizada e precisa sobre suas chances na vaga desejada. Boa sorte!
            </p>

          </div>
          <div class="my-2">
            <input type="file" class="file-input file-input-bordered file-input-primary my-1"
              @change="readFile" />
  
            <label class="input input-bordered flex items-center gap-2 mt-1">
              <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 16 16" fill="currentColor" class="w-4 h-4 opacity-70">
                <path
                  d="M8 8a3 3 0 1 0 0-6 3 3 0 0 0 0 6ZM12.735 14c.618 0 1.093-.561.872-1.139a6.002 6.002 0 0 0-11.215 0c-.22.578.254 1.139.872 1.139h9.47Z" />
              </svg>
              <input type="text" class="grow" placeholder="Link da Vaga" v-model="jobUrl" />
            </label>
          </div>
          <button class="btn btn-primary my-2 w-[100%]" :disabled="disableMatchBtn || isLoading" @click="checkJobMatch">
            <span v-if="isLoading" class="loading loading-spinner"></span>
            <span v-else>Match!</span>
          </button>
        </div>
  
        <div class="mockup-window border bg-secondary w-[90%] sm:w-[60%] mx-2 my-1">
          <div
            class="px-4 py-16 border-t border-base-300"
            v-html="matchFeedback"
          >
          </div>
        </div>
      </div>

    </div>
    <div class="drawer-side">
      <label for="my-drawer-2" aria-label="close sidebar" class="drawer-overlay"></label>
      <ul class="menu p-4 w-80 min-h-full bg-base-200 text-base-content">
        <p class="font-bold">Historico de Análises</p>
        <li>
          <p class="font-semibold">Em breve...</p>
        </li>
      </ul>
    </div>
  </div>
</template>


<script>
import { ofetch } from 'ofetch'
import MarkdownIt from "markdown-it";

const markdown = new MarkdownIt();

export default {
  props: {
    msg: String,
  },
  data: () => ({
    count: 0,
    response: '',
    jobUrl: null,
    resume: null,
    isLoading: false,
    matches: [],
  }),
  computed: {
    disableMatchBtn() {
      return !this.jobUrl || !this.resume
    },
    matchFeedback() {
      if (this.isLoading) return markdown.render('Aguarde... Estamos realizando a analise (aprox. 30 seg)')
      const feedback = this.response ? this.response : 'Aqui aparecerá o resultado do match com a vaga.'
      return markdown.render(feedback)
    }
  },
  watch: {
    count() {
      this.getData()
    }
  },
  mounted() {
    this.resume = localStorage.getItem('resume')
    this.matches = localStorage.getItem('matches')
  },
  methods: {
    async checkJobMatch() {
      this.isLoading = true
      const body = {
        resume: this.resume,
        job_url: this.jobUrl,
      }
      const response = await ofetch('https://api-job-ai-match.vercel.app/job-match', {
        method: 'POST',
        body,
      })
      this.response = response
      this.saveMatchOnLocalStorage(response)
      this.isLoading = false
    },
    async readFile(event) {
      console.log(event.target.files[0])
      const file = event.target.files[0]
      const form = new FormData()
      form.append('file', file)
      const response = await ofetch('https://api-job-ai-match.vercel.app/read_resume', {
        method: 'POST',
        body: form,
      })
      this.resume = response
      // this.saveResumeOnLocalStorage(response)
    },
    saveResumeOnLocalStorage(response) {
      localStorage.setItem('resume', response)
    },
    saveMatchOnLocalStorage(response) {
      const matches = localStorage.getItem('matches')
      const match = { text: response, date: new Date() }
      const newMatches = matches ? matches.push(match) : [match]
      localStorage.setItem('matches', newMatches)
      this.matches = newMatches
    },
    selectMatch(match) {
      this.response = match
    }
  }
}
</script>


<style scoped>
</style>
