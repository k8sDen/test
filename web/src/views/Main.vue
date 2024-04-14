<script setup lang="ts">
import FileUpload from "primevue/fileupload"
import Panel from "primevue/panel"
import Divider from "primevue/divider"
import Message from 'primevue/message';

const onUpload = () => {
  console.log(12)
}
</script>
<template>
  <div>
    <Message severity="success">Файл успешно загружен</Message>
    <Message severity="error">Ошибка при импорте</Message>
    <Panel header="Загрузка файла">
      <p class="m-0">
        Выберите файл для загрузки.
      </p>
      <FileUpload mode="basic" type="file" name="files[]" url="http://127.0.0.1/api/analytic/upload/" accept="application/vnd.ms-excel" :maxFileSize="1000000" @upload="onUpload" :auto="true"/>
    </Panel>
    <Divider/>
    <Panel header="Список отчетов">
      <li>
        <RouterLink to="/report/1">Report 1</RouterLink>
      </li>
    </Panel>

  </div>
</template>