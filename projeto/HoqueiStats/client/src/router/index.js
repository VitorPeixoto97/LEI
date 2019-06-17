import Vue from 'vue'
import Router from 'vue-router'

import Auth from '@/components/pages/Auth'
import Jogos from '@/components/pages/Jogos'
import Jogo from '@/components/pages/Jogo'
import Stats from '@/components/pages/Stats'
import Convocados from '@/components/pages/Convocados'
import Definicao from '@/components/pages/Definicao'
import StatsGame from '@/components/pages/StatsGame'
import StatsGameLive from '@/components/pages/StatsGameLive'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/jogos',
      name: 'Jogos',
      component: Jogos
    },
    {
      path: '/auth',
      name: 'Auth',
      component: Auth
    },
    {
      path: '/jogo',
      name: 'Jogo',
      component: Jogo
    },
    {
      path: '/stats',
      name: 'Stats',
      component: Stats
    },
    {
      path: '/convocados',
      name: 'Convocados',
      component: Convocados
    },
    {
      path: '/definicao',
      name: 'Definicao',
      component: Definicao
    },
    {
      path: '/statsgame',
      name: 'StatsGame',
      component: StatsGame
    },
    {
      path: '/statsgamelive',
      name: 'StatsGameLive',
      component: StatsGameLive
    }
  ]
})
