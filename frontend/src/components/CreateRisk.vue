<template>
        <div id="container" class="container">
            <div class="row">
                <div class="col-sm-8 offset-sm-2">
                <div class="alert alert-warning" v-show="showCreateMessage"  >
                  <button type="button" class="close" @click="hideMessage()">X</button>
                  <strong>Risk successfully created!</strong>
                </div>
                <div class="alert alert-warning" v-show="showUpdateMessage"  >
                  <button type="button" class="close" @click="hideMessage()">X</button>
                  <strong>Risk successfully updated!</strong>
                </div>
                <div class="alert alert-warning" v-show="showError"  >
                  <button type="button" class="close" @click="hideMessage()">X</button>
                  <strong>Error!</strong>
                </div>
                    <h1>Create a Risk</h1>
                    <div class="info-form">
                      <form>
                        <div class="form-group">
                          <label for="fieldName">Risk Name</label>
                          <input v-model="risk.name" type="text" class="form-control">
                          <small class="form-text text-muted">Enter risk name</small>
                          <label for="fieldName">Select Risk Type</label>
                          <select class="form-control" v-model="risk.risk_type" @change="onChange()" >
                            <option :value="null"></option>
                            <option v-bind:key="riskType.pk" v-for="riskType in riskTypes" v-bind:value="riskType.url">{{ riskType.name }}</option>
                          </select>
                          <div class="row">
                            <div class="col"><hr></div>
                          </div>
                          <div v-for="field in fields" v-bind:key="field.pk">
                            <label for="fieldName">{{field.name}}</label>
                            <input v-bind:ref="field.pk" v-if="field.type === 'text'"  type="text" class="form-control">
                            <small v-if="field.type === 'text'" class="form-text text-muted">text</small>
                            <select v-bind:ref="field.pk" v-if="field.type === 'enum'" class="form-control" >
                              <option v-for="optionValue in field.enumValues.split(',')" v-bind:key="optionValue" v-bind:value="optionValue" >{{ optionValue }}</option>
                            </select>
                            <small v-if="field.type === 'enum'" class="form-text text-muted">enum</small>
                            <input v-bind:ref="field.pk" v-if="field.type === 'date'" class="form-control" type="date">
                            <small v-if="field.type === 'date'" class="form-text text-muted">date</small>
                            <input v-bind:ref="field.pk" v-if="field.type === 'number'" class="form-control" type="number">
                            <small v-if="field.type === 'number'" class="form-text text-muted">number</small>
                          </div>
                        </div>
                      </form>
                       <button class="btn btn-primary" v-if="!this.risk.pk" @click="createRisk()" ><span v-if="!creating">Create</span><span v-if="creating">Creating... Please wait </span></button>
                       <button class="btn btn-primary" v-if="this.risk.pk" @click="updateRisk()" ><span v-if="!updating">Update</span><span v-if="updating">Updating... Please wait </span></button>
                    </div>
                </div>
            </div>
        </div>
</template>

<script>
/* eslint-disable */
function sleep (time) {
  return new Promise((resolve) => setTimeout(resolve, time));
}
import {APIService} from '../http/APIService';
const apiService = new APIService();
export default {
  name: 'RiskCreate',
  components: {
  },
  data() {
    return {
      showCreateMessage: false,
      showUpdateMessage: false,
      showError: false,
      risk: {},
      risks: '',
      creating: false,
      updating: false,
      riskTypes:[],
      fields: []
    };
  },
  methods: {
    hideMessage(){
      this.showCreateMessage = false;
      this.showUpdateMessage = false;
      this.showError = false;
    },
    onChange() {
      self = this
      self.fields = []

      apiService.getRiskTypesByURL(self.risk.risk_type).then((riskType) => {
        let urls = riskType.field
        urls.forEach(function(url)
        {
          apiService.getFieldsByURL(url).then((field) => {
            self.fields.push(field)
          });
        });
      });
    },
    createRisk(){
      this.creating = true;
      self = this;
      let fieldRisk = []
      let value
      self.fields.forEach(function(field)
      {
        if (field.type === "enum") {
          value = self.$refs[field.pk][0].selectedOptions[0].value

        } else {
          value = self.$refs[field.pk][0].value
        }
        fieldRisk.push({"field": field.url, "value": value})
      })
      let request = {"risk": this.risk, "fieldRisk": fieldRisk}

      console.log(request)
      apiService.createRisk(request).then((result)=>{
          console.log(result);
          // success
          if(result.status === 201){
            this.risk = {};
            this.showCreateMessage = true;
          }
            sleep(1000).then(() => {
               this.creating = false;
            })
      },(error)=>{
        this.showError = true;
            sleep(1000).then(() => {
               this.creating = false;
            })
      });
    },
    updateRisk(){
      this.updating = true;
      console.log('update risk' + JSON.stringify(this.risk));
      apiService.updateRisk(this.risk).then((result)=>{
          console.log(result);
          // success
          if(result.status === 200){
            this.risk = {};
            this.showUpdateMessage = true;
            sleep(1000).then(() => {
               this.updating = false;
            })
          }

      },(error)=>{
        this.showError = true;
        sleep(1000).then(() => {
               this.updating = false;
        })
      });
  },
    getRiskTypes(){
      this.loading = true;
      apiService.getRiskTypes().then((page) => {
        this.riskTypes = page.results;
        this.numberOfPages = page.total_pages;
        this.nextPageURL = page.next;
        if(this.numberOfPages)
        {
          for(var i = 2 ; i <= this.numberOfPages ; i++)
          {
            apiService.getRiskTypesByURL(this.nextPageURL).then((page) => {
              console.log("results");
              this.riskTypes.push(...page.results)
              this.nextPageURL = page.next;
            });
          }
       }
     });
    }
  },
  mounted() {
    this.getRiskTypes();
    if(this.$route.params.pk){
      console.log(this.$route.params.pk)
      apiService.getRisk(this.$route.params.pk).then((risk)=>{
        this.risk = risk;
      })
    }
  },
}
</script>
<style>
  @import '../assets/css/main.css';
</style>
