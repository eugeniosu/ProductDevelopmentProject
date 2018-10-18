import Vue from 'vue'
import Router from 'vue-router'
import CreateField from '@/components/CreateField'
import Field from '@/components/Field'
import CreateRiskType from '@/components/CreateRiskType'
import RiskType from '@/components/RiskType'
import Risk from '@/components/Risk'
import CreateRisk from '@/components/CreateRisk'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/field-list/',
      name: 'Home',
      component: Field
    },
    {
      path: '/field-create/',
      name: 'CreateField',
      component: CreateField
    },
    {
      path: '/field-update/:pk',
      name: 'UpdateField',
      component: CreateField
    },
    {
      path: '/risktype-list/',
      name: 'ListRiskType',
      component: RiskType
    },
    {
      path: '/riskType-update/:pk',
      name: 'UpdateRiskType',
      component: CreateRiskType
    },
    {
      path: '/risktype-create/',
      name: 'CreateRiskType',
      component: CreateRiskType
    },
    {
      path: '/',
      name: 'ListRisk',
      component: Risk
    },
    {
      path: '/risk-update/:pk',
      name: 'UpdateRisk',
      component: CreateRisk
    },
    {
      path: '/risk-create/',
      name: 'CreateRisk',
      component: CreateRisk
    }
  ]
})
