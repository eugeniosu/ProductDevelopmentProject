<template>
        <div id="container" class="container">
            <div class="row">
                <div class="col-sm-8 offset-sm-2">
                <div class="alert alert-warning" v-show="showCreateMessage"  >
                  <button type="button" class="close" @click="hideMessage()">X</button>
                  <strong>RiskType successfully created!</strong>
                </div>
                <div class="alert alert-warning" v-show="showUpdateMessage"  >
                  <button type="button" class="close" @click="hideMessage()">X</button>
                  <strong>RiskType successfully updated!</strong>
                </div>

                <div class="alert alert-warning" v-show="showError"  >
                  <button type="button" class="close" @click="hideMessage()">X</button>
                  <strong>Error!</strong>
                </div>
                    <h1>Create a RiskType</h1>
                    <div class="info-form">
                      <form>
                        <div class="form-group">
                          <label for="riskName">RiskType Name</label>
                          <input v-model="risk.name" type="text" class="form-control" id="riskName" placeholder="Enter RiskType Name">
                          <small id="riskHelp" class="form-text text-muted">Enter your attribute name</small>
                          <label for="exampleFormControlSelect1">Select Fields</label>
                          <select multiple class="form-control" v-model="risk.field" id="exampleFormControlSelect1">
                            <option v-bind:key="field.pk" v-for="field in fields" v-bind:value="field.url" >{{ field.name }}</option>
                          </select>
                        </div>
                      </form>
                       <button class="btn btn-primary" v-if="!this.risk.pk" @click="createRiskType()" ><span v-if="!creating">Create</span><span v-if="creating">Creating... Please wait </span></button>
                       <button class="btn btn-primary" v-if="this.risk.pk" @click="updateRiskType()" ><span v-if="!updating">Update</span><span v-if="updating">Updating... Please wait </span></button>
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
  name: 'RiskTypeCreate',
  components: {
  },
  data() {
    return {
      showCreateMessage: false,
      showUpdateMessage: false,
      showError: false,
      risk: {},
      riskTypes: '',
      creating: false,
      updating: false,
      fields:[]
    };
  },
  methods: {
    hideMessage(){
      this.showCreateMessage = false;
      this.showUpdateMessage = false;
      this.showError = false;
    },
    createRiskType(){
      console.log('create risk' + JSON.stringify(this.risk));
      this.creating = true;
      apiService.createRiskType(this.risk).then((result)=>{
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
    updateRiskType(){
      this.updating = true;
      console.log('update risk' + JSON.stringify(this.risk));
      apiService.updateRiskType(this.risk).then((result)=>{
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
    getFields(){
      this.loading = true;
      apiService.getFields().then((page) => {
        this.fields = page.results;
        this.numberOfPages = page.total_pages;
        this.nextPageURL = page.next;
        if(this.numberOfPages)
        {
          for(var i = 2 ; i <= this.numberOfPages ; i++)
          {

            apiService.getFieldsByURL(this.nextPageURL).then((page) => {
              console.log("results");
              this.fields.push(...page.results)
              this.nextPageURL = page.next;
            });
          }
       }
     });
    }
  },
  mounted() {
    this.getFields();
    if(this.$route.params.pk){
      console.log(this.$route.params.pk)
      apiService.getRiskType(this.$route.params.pk).then((risk)=>{
        this.risk = risk;
      })
    }
  },
}
</script>
<style>
  @import '../assets/css/main.css';
</style>
