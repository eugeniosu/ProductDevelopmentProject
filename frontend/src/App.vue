<template>
<div>
    <nav class="navbar navbar-expand-md navbar-dark bg-dark fixed-top">
      <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarCollapse" aria-controls="navbarCollapse" aria-expanded="false" aria-label="Toggle navigation">
        <span class="navbar-toggler-icon"></span>
      </button>
      <div class="collapse navbar-collapse" id="navbarCollapse">
        <ul class="navbar-nav mr-auto">
          <router-link class="nav-item" to="/">
              <a id="Risks" class="btn btn-primary active" href="/">Risks</a>
          </router-link>
          <router-link class="nav-item" to="/risktype-list">
            <a id="RiskTypes" class="btn btn-primary active">Risk Types</a>
          </router-link>
          <router-link class="nav-item" to="/field-list">
            <a id="Fields" class="btn btn-primary active" href="/">Fields</a>
          </router-link>
        </ul>
      </div>
    </nav>
    <router-view/>
</div>
</template>
<style>
@import './assets/css/bootstrap.min.css';
</style>
