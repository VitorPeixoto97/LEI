new Vue({
    el: '#starting',
    delimiters: ['${','}'],
    data: {
        atletas: [],
        loading: false,
        currentAtleta: {},
        message: null,
        newAtleta: { 'nome': null, 'licenca': null, 'camisola': null },
    },
    mounted: function() {
        this.getAtletas();
    },
    methods: {
        getClubes: function() {
            this.loading = true;
            this.$http.get('/rest/atleta/')
            .then((response) => {
                this.clubes = response.data;
                this.loading = false;
            })
            .catch((err) => {
                this.loading = false;
                console.log(err);
            })
        },
        getAtleta: function(id) {
            this.loading = true;
            this.$http.get('/rest/atleta/${id}/')
              .then((response) => {
                this.currentAtleta = response.data;
                this.loading = false;
              })
              .catch((err) => {
                this.loading = false;
                console.log(err);
              })
        },
        addAtleta: function() {
            this.loading = true;
            this.$http.post('/api/atleta/', this.newAtleta)
              .then((response) => {
                this.loading = false;
                this.getAtletas();
              })
              .catch((err) => {
                this.loading = false;
                console.log(err);
              })
        },
        updateAtleta: function() {
            this.loading = true;
            this.$http.put('/api/atleta/${this.currentAtleta.atleta_id}/', this.currentAtleta)
              .then((response) => {
                this.loading = false;
                this.currentAtleta = response.data;
                this.getAtletas();
              })
              .catch((err) => {
                this.loading = false;
                console.log(err);
              })
        },
        deleteAtleta: function(id) {
            this.loading = true;
            this.$http.delete('/api/atleta/${id}/' )
              .then((response) => {
                this.loading = false;
                this.getAtletas();
              })
              .catch((err) => {
                this.loading = false;
                console.log(err);
              })
        },
    }
});