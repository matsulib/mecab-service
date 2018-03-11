const http = axios.create({
    baseURL: '/api',
    headers: {'Content-Type': 'application/json'},
});

var mecab = Vue.extend({
    template: `<div id="mecab" class="container-fluid">
        <h2 class="page-header">
            Mecab
            <small>ipadic／mecab-ipadic-NEologd</small>
        </h2>
        <form class="form-inline container-fluid myForm">
            <label class="control-label"> 辞書を選択 : </label>
            <select class="form-control" v-model="selected">
                <option value="parse-ipadic">ipadic</option>
                <option value="parse-neologd">mecab-ipadic-NEologd</option>
            </select>
        </form>
        <form class="form-horizontal container-fluid">
            <div class="form-group">
                <div class="col-sm-10">
                    <textarea placeholder="テキストを入力" rows="3" class="form-control" id="InputTextarea" v-model="message"></textarea>
                </div>
            </div>
            <div class="text-center myForm"> 
                <input class="btn btn-primary" type="submit" value="送信" @click.prevent="submit">
            </div>
        </form>
        <table v-if="results" class="container-fluid table table-bordered">
            <thead>
                <tr>
                    <th v-for="col in columns">
                        {{ col }}
                    </th>
                </tr>
            </thead>
            <tbody>
                <tr v-for="word in results.results">
                    <td v-for="col in columns">
                        {{word[col]}}
                    </td>
                </tr>
            </tbody>
        </table>
        </div>`,
        data: function () {
            return {
                selected: "parse-ipadic",
                message: "",
                results: null,
                columns: ["原型", "品詞", "品詞細分類1", "活用型", "活用形", "発音", "読み"]
            }
        },
        methods: {
            submit: function () {
                http.post(`/${this.selected}`, {"sentence": this.message})
                    .then(response => {
                        this.results = response.data
                    })
                    .catch(error => {
                        console.log(error);
                    });
            }
        }
})


new Vue({
    el: '#app',
    components: {
        'mecab': mecab,
    },
    data: {
        ok: false
    },
    created: function () {
        if (FLASK_MECAB_URI) {
            this.ok = true;
        } else {
            alert('flask-mecab not found.');
        }
    }
})