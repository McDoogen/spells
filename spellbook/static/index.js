const app = Vue.createApp({
    compilerOptions: {
        delimiters: ["[[", "]]"]
    },
    data: function() {
        return {
            product: 'Socks',
            counter: 1,
            ing_list: ['600g Flour', '100g Salt', '237g Milk'],
            selected_category: "Nothing",
            some_var: "taco"
        }
    },
    methods: {
        add_to_counter() {
            this.counter += 1
        },
        select_category(cat) {
            this.selected_category = cat
        }
    }
}).mount("#app");