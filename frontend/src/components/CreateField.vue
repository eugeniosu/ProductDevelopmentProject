<template>
        <div id="container" class="container">
            <div class="row">
                <div class="col-sm-8 offset-sm-2">
                <div class="alert alert-warning" v-show="showCreateMessage"  >
                  <button type="button" class="close" @click="hideMessage()">X</button>
                  <strong>Field successfully created!</strong>
                </div>
                <div class="alert alert-warning" v-show="showUpdateMessage"  >
                  <button type="button" class="close" @click="hideMessage()">X</button>
                  <strong>Field successfully updated!</strong>
                </div>

                <div class="alert alert-warning" v-show="showError"  >
                  <button type="button" class="close" @click="hideMessage()">X</button>
                  <strong>Error!</strong>
                </div>
                    <h1>Create a Field</h1>
                    <div class="info-form">
                      <form>
                        <div class="form-group">
                          <label for="fieldName">Field Name</label>
                          <input v-model="field.name" type="text" class="form-control" id="fieldName" placeholder="Enter Field Name">
                          <small id="fieldHelp" class="form-text text-muted">Enter your attribute name</small>
                          <label for="exampleFormControlSelect1">Select Type</label>
                          <select class="form-control" v-model="field.type" id="exampleFormControlSelect1">
                              <option>text</option>
                              <option>number</option>
                              <option>date</option>
                              <option>enum</option>
                          </select>
                          <small class="form-text text-muted"></small>
                          <label for="fieldName">Enum Values</label>
                          <input :disabled="field.type !== 'enum'" v-model="field.enumValues" type="text" class="form-control" placeholder="Enter Enum values">
                          <small class="form-text text-muted">value1, value2, value3...</small>
                        </div>
                      </form>
                       <button class="btn btn-primary" v-if="!this.field.pk" @click="createField()" ><span v-if="!creating">Create</span><span v-if="creating">Creating... Please wait </span></button>
                       <button class="btn btn-primary" v-if="this.field.pk" @click="updateField()" ><span v-if="!updating">Update</span><span v-if="updating">Updating... Please wait </span></button>
                    </div>
                </div>
            </div>
        </div>

</template>

</template>

<script>
/* eslint-disable */
function sleep (time) {
  return new Promise((resolve) => setTimeout(resolve, time));
}
import {APIService} from '../http/APIService';
const apiService = new APIService();
export default {
  name: 'FieldCreate',
  components: {
  },
  data() {
    return {
      showCreateMessage: false,
      showUpdateMessage: false,
      showError: false,
      field: {},
      fields: '',
      creating: false,
      updating: false
    };
  },
  methods: {
    hideMessage(){
      this.showCreateMessage = false;
      this.showUpdateMessage = false;
      this.showError = false;
    },
    createField(){
      console.log('create field' + JSON.stringify(this.field));
      this.creating = true;
      apiService.createField(this.field).then((result)=>{
          console.log(result);
          // success
          if(result.status === 201){
            this.field = {};
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
    updateField(){
      this.updating = true;
      console.log('update field' + JSON.stringify(this.field));
      apiService.updateField(this.field).then((result)=>{
          console.log(result);
          // success
          if(result.status === 200){
            this.field = {};
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
    }
  },
  mounted() {

    if(this.$route.params.pk){
      console.log(this.$route.params.pk)
      apiService.getField(this.$route.params.pk).then((field)=>{
        this.field = field;
      })
    }
  },
}
</script>
<style>
  @import '../assets/css/main.css';
</style>
