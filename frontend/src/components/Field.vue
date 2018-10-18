<template>
<div>
<div class="row">
  <div class="col-sm-6"><h4>Fields (numberOfFields 3)</h4></div>
  <div class="col-sm-6"><h2 class="text-right text-warning">Eugenio Suarez qqqsmmskksks.</h2></div>
</div>

<router-link to="/field-create">
  <a class="btn btn-primary active">Create Field</a>
</router-link>
<Loading :loading="loading"></Loading>
<table class="table table-bordered table-hover">
  <thead>
    <tr>
      <th>#</th>
      <th>Name</th>
      <th>Type</th>
      <th>Created</th>
      <th>Actions</th>
    </tr>
  </thead>
  <tbody>
    <tr v-for="field in fields" @click="selectField(field)">
      <th>{{field.pk}}</th>
      <th>{{field.name}}</th>
      <th>{{field.type}}</th>
      <th>{{field.created}}</th>
      <td>
        <router-link :to="'/field-update/' + field.pk">
            <a class="btn btn-primary active"> &#9998; </a>
          </router-link>
        <button class="btn btn-danger" @click="deleteField(field)"> X</button>
      </td>
    </tr>
  </tbody>
</table>
<div>
<ul class="list-horizontal">
  <li><button class="btn btn-secondary" @click="getPreviousPage()">Previous</button></li>
  <li v-for="page in pages">
    <a class="btn btn-secondary" @click="getPage(page.link)">{{ page.pageNumber }}</a>
  </li>
  <li><button class="btn btn-secondary" @click="getNextPage()">Next</button></li>
</ul>
</div>
<div class="card text-center" v-if="selectedField">
  <div class="card-header">
    #{{selectedField.pk}} -- {{selectedField.name}}
  </div>
  <div class="card-block">
    <h4 class="card-title">{{selectedField.name}}</h4>
    <p class="card-text">
    {{selectedField.description}}
    </p>
    <a class="btn btn-primary" v-bind:href="'/field-update/' + selectedField.pk"> &#9998; </a>
    <button class="btn btn-danger" @click="deleteField(selectedField)"> X</button>
  </div>
</div>
</div>
</template>
<script>
/* eslint-disable */
import {APIService} from '../http/APIService';
import Loading from './Loading'
const API_URL = process.env.API;
const apiService = new APIService();
export default {
  name: 'FieldList',
  components: {
    Loading
  },
  data() {
    return {
      selectedField:null,
      fields: [],
      numberOfPages:0,
      pages : [],
      numberOfFields:0,
      loading: false,
      nextPageURL:'',
      previousPageURL:''
    };
  },
  methods: {
    getFields(){
      this.loading = true;
      apiService.getFields().then((page) => {
        this.fields = page.results;
        console.log(page);
        console.log(page.next);
        this.numberOfFields = page.count;
        this.numberOfPages = page.total_pages;
        this.nextPageURL = page.next;
        this.previousPageURL = page.previous;
        if(this.numberOfPages)
        {
          for(var i = 1 ; i <= this.numberOfPages ; i++)
          {
            const link =  `${API_URL}/api/field/?page=${i}`;
            console.log("link:"+link);
            this.pages.push({pageNumber: i , link: link})
          }
        }
        this.loading = false;
      });
    },
    getPage(link){
      this.loading = true;
      apiService.getFieldsByURL(link).then((page) => {
        this.fields = page.results;
        this.nextPageURL = page.next;
        this.previousPageURL = page.previous;
        this.loading = false;
      });
    },
    getNextPage(){
      console.log('next' + this.nextPageURL);
      this.loading = true;
      apiService.getFieldsByURL(this.nextPageURL).then((page) => {
        this.fields = page.results;
        this.nextPageURL = page.next;
        this.previousPageURL = page.previous;
        this.loading = false;
      });

    },
    getPreviousPage(){
      this.loading = true;
      apiService.getFieldsByURL(this.previousPageURL).then((page) => {
        this.fields = page.results;
        this.nextPageURL = page.next;
        this.previousPageURL = page.previous;
        this.loading = false;
      });

    },
    deleteField(field){
      console.log("deleting field: " + JSON.stringify(field))
      apiService.deleteField(field).then((r)=>{
        console.log(r);
        if(r.status === 204)
        {
          /*for(var i = this.products.length-1; i--;){
            console.log(this.products[i].pk);
            if (this.products[i].pk === product.pk)
            {
              console.log("deleting product " + this.products[i].pk)
              this.products.splice(i, 1);
            }
          }*/
          alert("Field deleted");
          this.$router.go()

        }
      })
    },
    selectField(field){
      this.selectedField = field;
    }
  },
  mounted() {

    this.getFields();
  },
}
</script>
<style>
  @import '../assets/css/main.css';
</style>
