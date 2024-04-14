<script setup lang="ts">
import {ref} from 'vue';
import DataTable from 'primevue/datatable';
import Column from 'primevue/column';
import ColumnGroup from 'primevue/columngroup';
import Row from 'primevue/row';
import InputText from 'primevue/inputtext';
import InputNumber from 'primevue/inputnumber';
import {FilterMatchMode, FilterOperator} from "primevue/api";
import type {FilterEvent, LazyParams, ReportTableRecord} from "@/types";

const filters = ref();
const loading = ref(false)
const first = ref(0);
const totalRecords = ref(0);

const lazyParams = ref<LazyParams>({
  first: 0,
  rows: 10
});

const records = ref<ReportTableRecord[]>([
  {
    id: 1,
    bank: 'АО "Народный сберегательный банк Казахстана"',
    actives: 14943264219,
    loan_portfolio_total: 9538649103,
    loan_portfolio_including_reverse_repo_operations: null,
    from_it_loans_with_late_payments_over_7_days_sum: 270896525,
    from_it_loans_with_late_payments_over_7_days_share_in_the_loan_portfolio: 2.84,
    from_it_loans_with_late_payments_over_30_days_sum: 237363333,
    from_it_loans_with_late_payments_over_30_days_share_in_the_loan_portfolio: 2.49,
    from_it_loans_with_late_payments_over_90_days_sum: 197106447,
    from_it_loans_with_late_payments_over_90_days_share_in_the_loan_portfolio: 2.07,
    amount_of_overdue_loans_including_overdue_remuneration: 156403205,
    provisions_formed_for_the_loan_portfolio_in_accordance_with_IFRS_requirements: 485032268,
    liabilities: 12548272708,
    of_which_contributions_individuals: 5697023282,
    of_which_contributions_legal_entities: 4993732403,
    equity_on_balance_sheet: 2394991511,
    excess_of_current_income_expenses_over_current_expenses_income_after_payment_of_income_tax: 673757575,
  },
]);

const initFilters = () => {
  filters.value = {
    bank: {operator: FilterOperator.AND, constraints: [{value: null, matchMode: FilterMatchMode.STARTS_WITH}]},
    actives: {operator: FilterOperator.AND, constraints: [{value: null, matchMode: FilterMatchMode.EQUALS}]},

  };
};
initFilters();


const loadLazyData = (event: FilterEvent) => {
  console.log('loadLazyData')
}
const onFilter = (event: FilterEvent) => {
  console.log('onFilter')
}

const onPage = (event: FilterEvent) => {
  console.log('onPage')
}
</script>

<template>
  <div class="card">
    <DataTable
        ref="dt"
        v-model:filters="filters"
        :value="records"
        :loading="loading"
        showGridlines
        filterDisplay="menu"
        dataKey="id"
        @filter="onFilter"
        @page="onPage"
        lazy
        paginator
        :first="first"
        :rows="10"
        :totalRecords="totalRecords"
    >
      <ColumnGroup type="header">
        <Row>
          <Column field="id" header="№" :rowspan="3"/>
          <Column field="bank" header="Наименование банка" :rowspan="3">
            <template #filter="{ filterModel }">
              <InputText v-model="filterModel.value" type="text" class="p-column-filter"/>
            </template>
          </Column>
          <Column header="Активы" :rowspan="3" filterField="actives" dataType="numeric">
            <template #body="{ data}">
              {{ data.actives }}
            </template>
            <template #filter="{ filterModel }">
              <InputNumber v-model="filterModel.value"/>
            </template>
          </Column>
          <Column header="Ссудный портфель" :colspan="2"/>
          <Column header="из него Кредиты с просрочкой платежей" :colspan="6"/>
          <Column header="Сумма просроченной задолженности по кредитам, включая просроченное вознаграждение" :rowspan="3"/>
          <Column header="Провизии, сформированные по ссудному портфелю в соответствии с требованиями МСФО" :rowspan="3"/>
          <Column header="Обязательства" :rowspan="3"/>
          <Column header="из них вклады" :colspan="2"/>
          <Column header="Собственный капитал по балансу" :rowspan="3"/>
          <Column header="Превышение текущих доходов (расходов) над текущими расходами (доходами) после уплаты подоходного налога" :rowspan="3"/>
        </Row>
        <Row>
          <Column header="всего" :rowspan="2"/>
          <Column header="в том числе"/>
          <Column header="свыше 7 дней" :colspan="2"/>
          <Column header="свыше 30 дней" :colspan="2"/>
          <Column header="свыше 90 дней" :colspan="2"/>
          <Column header="физических лиц" :rowspan="2"/>
          <Column header="юридических лиц" :rowspan="2"/>
        </Row>
        <Row>
          <Column header='операции "Обратное РЕПО"'/>
          <Column header="сумма"/>
          <Column header="доля  в ссудном портфеле"/>
          <Column header="сумма"/>
          <Column header="доля  в ссудном портфеле"/>
          <Column header="сумма"/>
          <Column header="доля  в ссудном портфеле"/>
        </Row>
      </ColumnGroup>
      <Column field="id" header="id"/>
      <Column field="bank" header="bank"/>
      <Column field="actives"/>
      <Column field="loan_portfolio_total"/>
      <Column field="loan_portfolio_including_reverse_repo_operations"/>
      <Column field="from_it_loans_with_late_payments_over_7_days_sum"/>
      <Column field="from_it_loans_with_late_payments_over_7_days_share_in_the_loan_portfolio"/>
      <Column field="from_it_loans_with_late_payments_over_30_days_sum"/>
      <Column field="from_it_loans_with_late_payments_over_30_days_share_in_the_loan_portfolio"/>
      <Column field="from_it_loans_with_late_payments_over_90_days_sum"/>
      <Column field="from_it_loans_with_late_payments_over_90_days_share_in_the_loan_portfolio"/>
      <Column field="amount_of_overdue_loans_including_overdue_remuneration"/>
      <Column field="provisions_formed_for_the_loan_portfolio_in_accordance_with_IFRS_requirements"/>
      <Column field="liabilities"/>
      <Column field="of_which_contributions_individuals"/>
      <Column field="of_which_contributions_legal_entities"/>
      <Column field="equity_on_balance_sheet"/>
      <Column field="excess_of_current_income_expenses_over_current_expenses_income_after_payment_of_income_tax"/>
    </DataTable>
  </div>
</template>

<style scoped>

</style>