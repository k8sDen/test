<script setup lang="ts">
import {onMounted, computed} from 'vue'
import FileUpload from 'primevue/fileupload'
import Panel from 'primevue/panel'
import Divider from 'primevue/divider'
import ProgressSpinner from 'primevue/progressspinner'
import Message from 'primevue/message'
import {useReports} from '@/composables/useReports'

const {fetchReports, reports, isLoadingReport, onUpload, message, error} = useReports()

onMounted(() => {
  fetchReports()
})
</script>
<template>
  <div>
    <Message severity="success" v-if="message">{{ message }}</Message>
    <Message severity="error" v-if="error">{{ error }}</Message>
    <Divider/>
    <Panel header="Загрузка файла">
      <p class="m-0">
        Выберите файл для загрузки.
      </p>
      <FileUpload
          mode="basic"
          name="files[]"
          :auto="true"
          :customUpload="true"
          accept="application/vnd.ms-excel"
          @uploader="onUpload"
      />
    </Panel>
    <Divider/>
    <Panel header="Список отчетов">
      <ProgressSpinner v-if="isLoadingReport"/>
      <div v-else>
        <ul v-if="reports.length > 0">
          <li v-for="(report,index) in reports" :key="index">
            <RouterLink :to="`/report/${report.id}`">{{ report.id }}. {{ report.title }}</RouterLink>
          </li>
        </ul>
        <div v-else>Пусто</div>
      </div>
    </Panel>

  </div>
</template>
