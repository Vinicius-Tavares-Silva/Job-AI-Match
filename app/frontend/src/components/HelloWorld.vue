<template>
  <h1>{{ msg }}</h1>

  <div class="card">
    <button type="button" @click="count++">count is {{ count }}</button>
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
    response: ''
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
    }
  }
}
</script>

<style scoped>
.read-the-docs {
  color: #888;
}
</style>
