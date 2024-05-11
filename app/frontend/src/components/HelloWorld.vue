<template>
  <h1>{{ msg }}</h1>

  <div class="card">
    <button type="button" @click="count++">count is {{ count }}</button>
    <!-- <input type="file" @change="readResume">Enviar Curriculo</input> -->
    <button type="button" @click="checkJobMatch">Match com vaga</button>
    <p>
      Edit
      <code>components/HelloWorld.vue</code> to test HMR
    </p>
  </div>

  <p>
    Check out
    <a href="https://vuejs.org/guide/quick-start.html#local" target="_blank"
      >create-vue</a
    >, the official Vue + Vite starter
  </p>
  <p>
    Install
    <a href="https://github.com/vuejs/language-tools" target="_blank">Volar</a>
    in your IDE for a better DX
  </p>
  <p class="read-the-docs">Click on the Vite and Vue logos to learn more</p>
  <p class="read-the-docs">response: {{ response }}</p>
</template>

<script>
import { ofetch } from 'ofetch'
export default {
  props: {
    msg: String,
  },
  data: () => ({
    count: 0,
    response: '',
    cv: 'Dados do Currículo de Vinícius Tavares da Silva:Informações de Contato:Telefone: 11975051557Email: vini_tavares10@hotmail.comLinkedIn: www.linkedin.com/in/vinicius-tavares-da-silvaPortfólio: vinicius-tavares-silva.github.io/GitHub: github.com/Vinicius-Tavares-SilvaFacebook: www.facebook.com/vinicius.tavares.3133/Resumo:Vinícius é um desenvolvedor apaixonado por tecnologia e programação, buscando gerar impacto positivo através de seu trabalho. Ele fez uma transição de carreira para desenvolvimento web e está aprimorando suas habilidades através da Trybe.Habilidades:Desenvolvimento de SoftwareFront-end: Vue.js / React.jsFullStack: Node.jsMicrosoft ExcelComprometimentoExperiência Profissional:Desenvolvedor Web Front-End na Omie (outubro de 2021 - presente):2 anos e 8 meses de experiência.Local: São Paulo, Brasil.Analista de Projetos no Itaú Unibanco (agosto de 2018 - abril de 2021):2 anos e 9 meses de experiência.Local: São Paulo, Brasil.Responsabilidades:Gestão de projetos de desenvolvimento de software.Suporte a sistemas da área de negócio (Automações).Mapeamento de processos e identificação de oportunidades de negócios.Especificação e homologação de demandas de TI.Estagiário no Itaú Unibanco (julho de 2017 - agosto de 2018):1 ano e 2 meses de experiência.Local: São Paulo, Brasil.Responsabilidades:Controle e acompanhamento de projetos.Mapeamento de processos e identificação de oportunidades de negócios.Especificação e homologação de demandas de TI.Formação Acadêmica:Trybe: Tecnologia da Informação (abril de 2021 - abril de 2022).Centro Universitário do Instituto Mauá de Tecnologia: Bacharelado em Engenharia Mecatrônica, Robótica e Engenharia de Controle e Automação (janeiro de 2013 - dezembro de 2018).University of Technology Sydney: Mecatrônica, Robótica e Engenharia de Controle e Automação (janeiro de 2015 - fevereiro de 2015).',
    job: 'SoftwareEngineerII,Front-End-UberFlashandDirect(Uber-GrandeSãoPaulo)Sobreavaga:AUberestábuscandoum(a)SoftwareEngineerIIcomfocoemFront-EndparasejuntaraotimedoUberFlashandDirectemSãoPaulo.Vocêirácolaborarcomumaequipetalentosadeengenheiros,gerentesdeprodutoedesignersparadesenvolvereaprimorarsoluçõeswebparamilharesdeclientes.Responsabilidades:Desenvolver,projetarcaprimorarinterfacesdeusuárioerecursosparaaplicaçõeswebqueatendamàsnecessidadesdedesign,funcionalidadeecomplexidadedosusuáriosfinais,focandonosprodutosUberDirecteUberConnect.Escrevercódigodealtaqualidadeeseguirospadrõesdetestesecobertura.Alinhar aequipe naresoluçãodeproblemasambíguoseanalisarascompensaçõesdeferentessoluções técnicas.Contribuirparaaculturadeengenhariaemtermosdequalidade,monitoramentoepráticasdeplantão.Identificaroportunidadesparamelhoro funcionamentodaequipeepromoverprocessospadronizados.RequisitosMínimos:BachareladoouequivalenteemCiência daComputação,Engenharia,MatemáticaouárearelacionadaOU3+anosdeexperiênciaemengenhariadesoftware.DomínioemlinguagensdeprogramaçãocomoReact,JavaScripteCSS.Inglês(conversação).HabilidadesTécnicas:EngenhariadeprodutoEngenhariadescalabilidadeSistemasdistribuídosDesign deAPIJavascript modernoReactSobreaEquipe:UberConnecteDirectsãoprodutosderápidocrescimentonosmercadosC2C(ConsumidorparaConsumidor)eB2C(EmpresaparaConsumidor),respectivamente.OUberDirectéumasolução deentreganonívelempresarialquepermiteaoscomerciantescriarentregasusandoopaineldoprodutoouintegrandodiretamenteaAPIpública.Observações:Aexperiênciatotalde3anosemengenhariadesoftwarepodetersidoadquiridapormeiodeeducaçãoeexperiênciaprofissionalemtempointegral,treinamentoadicional,cursos,pesquisaousimilar.Osanosdeexperiênciasespecializadanãosãonecessariamenteadicionaisaosanosdeeducaçãoeexperiênciaprofissionalemtempointegralindicados.Benefícios:AUberofereceumpacotedebenefícioscompetitivo,incluindosalário,benefíciosdesaúde,planodeaposentadoriaeoportunidadesdecrescimentoprofissional.Candidatura:VocêpodesecandidataràvagadiretamentepeloLinkedinou pelositedaUber.',
  }),
  watch: {
    count() {
      this.getData()
    }
  },
  methods: {
    async getData() {
      const response = await ofetch(`https://job-ai-match-backend.vercel.app/items/${this.count}?q=somequery`)
      console.log(response)
      this.response = response
    },
    async readResume(event) {
      console.log(event.target.value);
      // const response = await ofetch('http://localhost:5000/readResume', {
      //   method: 'POST',
      //   body: this.cv,
      // })
      // console.log(response)
      // this.response = response
    },
    async checkJobMatch() {
      const body = {
        cv: this.cv,
        job: this.job,
      }
      const response = await ofetch('https://job-ai-match-backend.vercel.app/job-match', {
        method: 'POST',
        body,
      })
      console.log(response)
      this.response = response
    },
  }
}
</script>

<style scoped>
.read-the-docs {
  color: #888;
}
</style>
