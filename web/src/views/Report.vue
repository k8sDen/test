<script setup lang="ts">
import {useReport} from '@/composables/useReport'
import DataTable from 'primevue/datatable';
import Column from 'primevue/column';
import Button from 'primevue/button';
import ColumnGroup from 'primevue/columngroup';
import Row from 'primevue/row';
import InputText from 'primevue/inputtext';
import InputNumber from 'primevue/inputnumber';
import {onMounted} from 'vue'

const {isLoading, filters, first, totalRecords, records, initFilters, onFilter, onPage, loadLazyData, onSort} = useReport()

initFilters();

onMounted(() => {
  loadLazyData()
})
</script>

<template>
  <div class="card">
    <Button label="Назад" link @click="$router.back()"/>
    <DataTable
        ref="dt"
        v-model:filters="filters"
        :value="records"
        :loading="isLoading"
        showGridlines
        filterDisplay="menu"
        dataKey="report_bank_id"
        @filter="onFilter"
        @page="onPage"
        @sort="onSort"
        lazy
        paginator
        :first="first"
        :rows="10"
        :totalRecords="totalRecords"
    >
      <ColumnGroup type="header">
        <Row>
          <Column field="id" header="№" :rowspan="3" sortable/>
          <Column field="title" header="Наименование банка" :rowspan="3" sortable>
            <template #filter="{ filterModel }">
              <InputText v-model="filterModel.value" type="text" class="p-column-filter"/>
            </template>
          </Column>
          <Column header="Активы" :rowspan="3" filter-field="actives">
            <template #filter="{ filterModel }">
              <InputNumber v-model="filterModel.value"/>
            </template>
          </Column>
          <Column header="Ссудный портфель" :colspan="2"/>
          <Column header="из него Кредиты с просрочкой платежей" :colspan="6"/>
          <Column header="Сумма просроченной задолженности по кредитам, включая просроченное вознаграждение"
                  :rowspan="3"
                  filter-field="amount_remuneration"
          >
            <template #filter="{ filterModel }">
              <InputNumber v-model="filterModel.value"/>
            </template>
          </Column>
          <Column header="Провизии, сформированные по ссудному портфелю в соответствии с требованиями МСФО"
                  :rowspan="3"
                  filter-field="provision_requirements"
          >
            <template #filter="{ filterModel }">
              <InputNumber v-model="filterModel.value"/>
            </template>
          </Column>
          <Column header="Обязательства" :rowspan="3" filter-field="liabilities">
            <template #filter="{ filterModel }">
              <InputNumber v-model="filterModel.value"/>
            </template>
          </Column>
          <Column header="из них вклады" :colspan="2"/>
          <Column header="Собственный капитал по балансу" :rowspan="3" filter-field="equity_on_balance_sheet">
            <template #filter="{ filterModel }">
              <InputNumber v-model="filterModel.value"/>
            </template>
          </Column>
          <Column header="Превышение текущих доходов (расходов) над текущими расходами (доходами) после уплаты подоходного налога"
                  :rowspan="3"
                  filter-field="excess_of_income_tax">
            <template #filter="{ filterModel }">
              <InputNumber v-model="filterModel.value"/>
            </template>
          </Column>
        </Row>
        <Row>
          <Column header="всего" :rowspan="2" filter-field="loan_portfolio_total">
            <template #filter="{ filterModel }">
              <InputNumber v-model="filterModel.value"/>
            </template>
          </Column>
          <Column header="в том числе"/>
          <Column header="свыше 7 дней" :colspan="2"/>
          <Column header="свыше 30 дней" :colspan="2"/>
          <Column header="свыше 90 дней" :colspan="2"/>
          <Column header="физических лиц" :rowspan="2" filter-field="contributions_individuals">
            <template #filter="{ filterModel }">
              <InputNumber v-model="filterModel.value"/>
            </template>
          </Column>
          <Column header="юридических лиц" :rowspan="2" filter-field="contributions_legal_entities">
            <template #filter="{ filterModel }">
              <InputNumber v-model="filterModel.value"/>
            </template>
          </Column>
        </Row>
        <Row>
          <Column header='операции "Обратное РЕПО"' filter-field="reverse_repo_operations">
            <template #filter="{ filterModel }">
              <InputNumber v-model="filterModel.value"/>
            </template>
          </Column>
          <Column header="сумма" filter-field="late_payments_7_sum">
            <template #filter="{ filterModel }">
              <InputNumber v-model="filterModel.value"/>
            </template>
          </Column>
          <Column header="доля  в ссудном портфеле" filter-field="late_payments_7_portfolio">
            <template #filter="{ filterModel }">
              <InputNumber v-model="filterModel.value" :minFractionDigits="2"/>
            </template>
          </Column>
          <Column header="сумма" filter-field="late_payments_30_sum">
            <template #filter="{ filterModel }">
              <InputNumber v-model="filterModel.value"/>
            </template>
          </Column>
          <Column header="доля  в ссудном портфеле" filter-field="late_payments_30_portfolio">
            <template #filter="{ filterModel }">
              <InputNumber v-model="filterModel.value"/>
            </template>
          </Column>
          <Column header="сумма" filter-field="late_payments_90_sum">
            <template #filter="{ filterModel }">
              <InputNumber v-model="filterModel.value"/>
            </template>
          </Column>
          <Column header="доля  в ссудном портфеле" filter-field="late_payments_90_portfolio">
            <template #filter="{ filterModel }">
              <InputNumber v-model="filterModel.value"/>
            </template>
          </Column>
        </Row>
      </ColumnGroup>
      <Column field="id"/>
      <Column field="title"/>
      <Column field="actives"/>
      <Column field="loan_portfolio_total"/>
      <Column field="reverse_repo_operations"/>
      <Column field="late_payments_7_sum"/>
      <Column field="late_payments_7_portfolio"/>
      <Column field="late_payments_30_sum"/>
      <Column field="late_payments_30_portfolio"/>
      <Column field="late_payments_90_sum"/>
      <Column field="late_payments_90_portfolio"/>
      <Column field="amount_remuneration"/>
      <Column field="provision_requirements"/>
      <Column field="liabilities"/>
      <Column field="contributions_individuals"/>
      <Column field="contributions_legal_entities"/>
      <Column field="equity_on_balance_sheet"/>
      <Column field="excess_of_income_tax"/>
    </DataTable>
  </div>
</template>

<style scoped>

</style>
