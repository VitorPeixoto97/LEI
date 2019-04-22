window.$ = window.jQuery = require('jquery');
require('bootstrap-sass');
import Vue from 'vue';

import Demo from "./components/Demo.vue";

const app = new Vue({
    el: '#app',
    components: {
        Demo
    }
});

const clube = new Vue({
    el: '#clube',
    components: {
        Clube
    },
    data: {
        nome,
        cor,
        simbolo
    },
    methods: {
        onFileChanged (event) {
            simbolo = event.target.files[0]
        },
        onSubmit(event) {
            let newClube = {
                nome: this.nome,
                cor: this.cor,
                simbolo: this.simbolo
            }
            event.preventDefault()
            alert(JSON.stringify(newClube))
        }
    }
});

const gClube = new Vue({
    el: '#gClube',
    data: {
        info : null
    },
    components: {
        gClube
    },
    methods: {
        created: function () {
            /*currentLocation = window.location.href;
            split = currentLocation.split('/');
            nome = split[5];
            cor = split[6];
            simbolo = split[7];*/
            axios
                .get(window.location.href + '/clube/json')
                .then(response => (this.data = response.json()))
        }
    }
})