<template>
  <header>
    <h1> {{ spell_name }} </h1>
    <h3> by: {{ author }} </h3>
  </header>
  <aside>
    <ol>
        <li v-for="ingredient in ingredients" v-bind:key="ingredient.name">
          {{ ingredient }}
        </li>
    </ol>
  </aside>
  <section>
      <h4>Process</h4>
  </section>
</template>

<script>

export default {
  name: 'App',
  data: function() {
    return {
      spell_name: "",
      author: "",
      ingredients: ""
    }
  },
  created: async function() {
    const gResponse = await fetch("http://localhost:5000/test");
    const gObject = await gResponse.json();
    this.spell_name = gObject.spell_name;
    this.author = gObject.author;
    this.ingredients = gObject.ingredients;
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
  padding: 60px;

  background: #aaaaaa;
  display: grid;
  width: 1000px;
  height: 800px;
  grid-template-areas:
  "h h"
  "a s";
  grid-template-rows: 150px 1fr;
  grid-template-columns: 200px 1fr;
}
#app > header {
    background: #8ca0ff;
    grid-area: h;
    text-align: center;
}

#app > aside {
    background: #71ff64;
    grid-area: a;
    text-align: left;
}

#app > section {
    background: #ffff64;
    grid-area: s;
}
</style>
