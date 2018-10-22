<template>
  <div>
    <div class="row">
      <div class="col-sm-6"><h4>Risks</h4></div>
      <div class="col-sm-6"><h2 class="text-right text-warning">Eugenio Suarez.</h2></div>
    </div>

    <router-link  to="/risk-create">
      <a id="CreateRisk" class="btn btn-primary active">Create Risk</a>
    </router-link>
    <Loading :loading="loading"></Loading>
    <table class="table table-bordered table-hover">
      <thead>
        <tr>
          <th>#</th>
          <th>Name</th>
          <th>Description</th>
          <th>RiskType</th>
          <th>Created</th>
          <th>Actions</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="risk in risks" v-bind:key="risk.pk" @click="selectRisk(risk)">
          <th>{{risk.pk}}</th>
          <th>{{risk.name}}</th>
          <th>{{risk.description}}</th>
          <th>{{risk.risk_type}}</th>
          <th>{{risk.created}}</th>
          <td>
            <router-link :to="'/risk-update/' + risk.pk">
                <a class="btn btn-primary active"> &#9998; </a>
              </router-link>
            <button class="btn btn-danger" @click="deleteRisk(risk)"> X</button>
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
    <div class="card text-center" v-if="selectedRisk">
      <div class="card-header">
        #{{selectedRisk.pk}} -- {{selectedRisk.name}}
      </div>
      <div class="card-block">
        <h4 class="card-title">{{selectedRisk.name}}</h4>
        <p class="card-text">
        {{selectedRisk.description}}
        </p>
        <a class="btn btn-primary" v-bind:href="'/risk-update/' + selectedRisk.pk"> &#9998; </a>
        <button class="btn btn-danger" @click="deleteRisk(selectedRisk)"> X</button>
      </div>
    </div>
  </div>
</template>
<script>
/* eslint-disable */
import {APIService} from '../http/APIService';
import Loading from './Loading'
const API_URL = 'https://zfex100uxi.execute-api.us-east-1.amazonaws.com/dev';
const apiService = new APIService();
export default {
  name: 'RiskList',
  components: {
    Loading
  },
  data() {
    return {
      selectedRisk:null,
      risks: [],
      numberOfPages:0,
      pages : [],
      numberOfRisks:0,
      loading: false,
      nextPageURL:'',
      previousPageURL:''
    };
  },
  methods: {
    getRisks(){
      this.loading = true;
      apiService.getRisks().then((page) => {
        this.risks = page.results;
        console.log(page);
        console.log(page.next);
        this.numberOfRisks = page.count;
        this.numberOfPages = page.total_pages;
        this.nextPageURL = page.next;
        this.previousPageURL = page.previous;
        if(this.numberOfPages)
        {
          for(var i = 1 ; i <= this.numberOfPages ; i++)
          {
            const link =  `${API_URL}/api/risk/?page=${i}`;
            console.log("link:"+link);
            this.pages.push({pageNumber: i , link: link})
          }
        }
        this.loading = false;
      });
    },
    getPage(link){
      this.loading = true;
      apiService.getRisksByURL(link).then((page) => {
        this.risks = page.results;
        this.nextPageURL = page.next;
        this.previousPageURL = page.previous;
        this.loading = false;
      });
    },
    getNextPage(){
      console.log('next' + this.nextPageURL);
      this.loading = true;
      apiService.getRisksByURL(this.nextPageURL).then((page) => {
        this.risks = page.results;
        this.nextPageURL = page.next;
        this.previousPageURL = page.previous;
        this.loading = false;
      });

    },
    getPreviousPage(){
      this.loading = true;
      apiService.getRisksByURL(this.previousPageURL).then((page) => {
        this.risks = page.results;
        this.nextPageURL = page.next;
        this.previousPageURL = page.previous;
        this.loading = false;
      });

    },
    deleteRisk(risk){
      console.log("deleting risk: " + JSON.stringify(risk))
      apiService.deleteRisk(risk).then((r)=>{
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
          alert("Risk deleted");
          this.$router.go()

        }
      })
    },
    selectRisk(risk){
      this.selectedRisk = risk;
    }
  },
  mounted() {

    this.getRisks();
  },
}
</script>
<style>
  @import '../assets/css/main.css';
</style>
