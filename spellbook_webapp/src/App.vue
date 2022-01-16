<template>
  <div id="fire-box">
    <img src="./assets/fire.gif" />
  </div>
  <div id="spell-scroll">
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
  </div>
  <div id="fire-box">
    <img src="./assets/fire.gif"/>
  </div>
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
body {
  overflow: hidden;
  margin: 0;
}
#app {
  display: grid;
  grid-template-columns: 1fr 3fr 1fr;
  width: 100vw;
  height: 100vh;
  background: black;
}
#fire-box {
  display: flex;
  align-items: center;
}

#spell-scroll {
  font: italic 1em "The Nautigal", cursive;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  padding: 20px 80px 20px 80px;

  background-image: url("./assets/scroll.png");
  background-color: black;
  background-size: 100%;
  background-position-y: -90px;
  display: grid;
  grid-template-areas:
  "h h"
  "a s";
  grid-template-rows: 150px 1fr;
  grid-template-columns: 200px 1fr;
}
#spell-scroll > header {
  background: #8ca0ffaa;
  grid-area: h;
  text-align: center;
}

#spell-scroll > aside {
  background: #71ff64aa;
  grid-area: a;
  text-align: left;
}

#spell-scroll > section {
  background: #ffff64aa;
  grid-area: s;
}
</style>
