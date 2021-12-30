<template>
  <div id='app'>
    <p>{{ greeting }}</p>
    <p>{{ flaskGreeting }}</p>
    <img alt="Vue logo" src="./assets/logo.png">
    <HelloWorld msg="Welcome to Your Vue.js App"/>
  </div>
</template>

<script>
import HelloWorld from './components/HelloWorld.vue'

export default {
  name: 'App',
  components: {
    HelloWorld
  },
  data: function() {
    return {
      greeting: "Hello, Vue!",
      flaskGreeting: ""
    }
  },
  created: async function() {
    const gResponse = await fetch("http://localhost:5000/test");
    const gObject = await gResponse.json();
    this.flaskGreeting = gObject.greeting;
  }
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
