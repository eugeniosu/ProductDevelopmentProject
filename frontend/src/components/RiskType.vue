<template>
<div>
<div class="row">
  <div class="col-sm-6"><h4>RiskTypes</h4></div>
  <div class="col-sm-6"><h2 class="text-right text-warning">Eugenio Suarez.</h2></div>
</div>

<router-link  to="/riskType-create">
  <a id="CreateRiskType" class="btn btn-primary active">Create RiskType</a>
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
    <tr v-for="riskType in riskTypes" v-bind:key="riskType.pk" @click="selectRiskType(riskType)">
      <th>{{riskType.pk}}</th>
      <th>{{riskType.name}}</th>
      <th>{{riskType.created}}</th>
      <td>
        <router-link :to="'/riskType-update/' + riskType.pk">
            <a class="btn btn-primary active"> &#9998; </a>
          </router-link>
        <button class="btn btn-danger" @click="deleteRiskType(riskType)"> X</button>

      </td>
    </tr>
  </tbody>
</table>
<div>
<ul class="list-horizontal">
  <li><button class="btn btn-secondary" @click="getPreviousPage()">Previous</button></li>
  <li v-for="page in pages" v-bind:key="page.pageNumber">
    <a class="btn btn-secondary" @click="getPage(page.link)">{{ page.pageNumber }}</a>
  </li>
  <li><button class="btn btn-secondary" @click="getNextPage()">Next</button></li>
</ul>
</div>
<div class="card text-center" v-if="selectedRiskType">
  <div class="card-header">
    #{{selectedRiskType.pk}} -- {{selectedRiskType.name}}
  </div>
  <div class="card-block">
    <h4 class="card-title">{{selectedRiskType.name}}</h4>
    <p class="card-text">
    {{selectedRiskType.description}}
    </p>
    <a class="btn btn-primary" v-bind:href="'/riskType-update/' + selectedRiskType.pk"> &#9998; </a>
    <button class="btn btn-danger" @click="deleteRiskType(selectedRiskType)"> X</button>
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
  name: 'RiskTypeList',
  components: {
    Loading
  },
  data() {
    return {
      selectedRiskType:null,
      riskTypes: [],
      numberOfPages:0,
      pages : [],
      numberOfRiskTypes:0,
      loading: false,
      nextPageURL:'',
      previousPageURL:''
    };
  },
  methods: {
    getRiskTypes(){
      this.loading = true;
      apiService.getRiskTypes().then((page) => {
        this.riskTypes = page.results;
        console.log(page);
        console.log(page.next);
        this.numberOfRiskTypes = page.count;
        this.numberOfPages = page.total_pages;
        this.nextPageURL = page.next;
        this.previousPageURL = page.previous;
        if(this.numberOfPages)
        {
          for(var i = 1 ; i <= this.numberOfPages ; i++)
          {
            const link =  `${API_URL}/api/riskType/?page=${i}`;
            console.log("link:"+link);
            this.pages.push({pageNumber: i , link: link})
          }
        }
        this.loading = false;
      });
    },
    getPage(link){
      this.loading = true;
      apiService.getRiskTypesByURL(link).then((page) => {
        this.riskTypes = page.results;
        this.nextPageURL = page.next;
        this.previousPageURL = page.previous;
        this.loading = false;
      });
    },
    getNextPage(){
      console.log('next' + this.nextPageURL);
      this.loading = true;
      apiService.getRiskTypesByURL(this.nextPageURL).then((page) => {
        this.riskTypes = page.results;
        this.nextPageURL = page.next;
        this.previousPageURL = page.previous;
        this.loading = false;
      });

    },
    getPreviousPage(){
      this.loading = true;
      apiService.getRiskTypesByURL(this.previousPageURL).then((page) => {
        this.riskTypes = page.results;
        this.nextPageURL = page.next;
        this.previousPageURL = page.previous;
        this.loading = false;
      });

    },
    deleteRiskType(riskType){
      console.log("deleting riskType: " + JSON.stringify(riskType))
      apiService.deleteRiskType(riskType).then((r)=>{
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
          alert("RiskType deleted");
          this.$router.go()

        }
      })
    },
    selectRiskType(riskType){
      this.selectedRiskType = riskType;
    }
  },
  mounted() {

    this.getRiskTypes();
  },
}
</script>
<style>
  @import '../assets/css/main.css';
</style>
