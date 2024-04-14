import {createApp} from 'vue'
import {createPinia} from 'pinia'
import PrimeVue from 'primevue/config';
import 'primevue/resources/themes/aura-light-green/theme.css'

import App from './App.vue'
import router from './router'
import ruLocale from '@/utils/prime.ru.json'

const app = createApp(App)

app.use(createPinia())
app.use(router)
app.use(PrimeVue, {
    locale: ruLocale
})

app.mount('#app')
