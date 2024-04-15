import api from '@/helpers/api'
import type {ReportTableRecord} from '@/types'
import {FilterOperator, FilterMatchMode} from 'primevue/api'
import {ref} from 'vue'
import {useRoute} from 'vue-router'

export const useReport = () => {
    const route = useRoute()
    const isLoading = ref(false)
    const filters = ref()
    const first = ref(0);
    const totalRecords = ref(0);

    let lazyParams = {
        filters: {},
    };

    const records = ref<ReportTableRecord[]>([]);

    const initFilters = () => {
        filters.value = {
            title: {operator: FilterOperator.AND, constraints: [{value: null, matchMode: FilterMatchMode.CONTAINS}]},
            actives: {operator: FilterOperator.AND, constraints: [{value: null, matchMode: FilterMatchMode.EQUALS}]},
            loan_portfolio_total: {operator: FilterOperator.AND, constraints: [{value: null, matchMode: FilterMatchMode.EQUALS}]},
            reverse_repo_operations: {operator: FilterOperator.AND, constraints: [{value: null, matchMode: FilterMatchMode.EQUALS}]},
            late_payments_7_sum: {operator: FilterOperator.AND, constraints: [{value: null, matchMode: FilterMatchMode.EQUALS}]},
            late_payments_7_portfolio: {operator: FilterOperator.AND, constraints: [{value: null, matchMode: FilterMatchMode.EQUALS}]},
            late_payments_30_sum: {operator: FilterOperator.AND, constraints: [{value: null, matchMode: FilterMatchMode.EQUALS}]},
            late_payments_30_portfolio: {operator: FilterOperator.AND, constraints: [{value: null, matchMode: FilterMatchMode.EQUALS}]},
            late_payments_90_sum: {operator: FilterOperator.AND, constraints: [{value: null, matchMode: FilterMatchMode.EQUALS}]},
            late_payments_90_portfolio: {operator: FilterOperator.AND, constraints: [{value: null, matchMode: FilterMatchMode.EQUALS}]},
            amount_remuneration: {operator: FilterOperator.AND, constraints: [{value: null, matchMode: FilterMatchMode.EQUALS}]},
            provision_requirements: {operator: FilterOperator.AND, constraints: [{value: null, matchMode: FilterMatchMode.EQUALS}]},
            liabilities: {operator: FilterOperator.AND, constraints: [{value: null, matchMode: FilterMatchMode.EQUALS}]},
            contributions_individuals: {operator: FilterOperator.AND, constraints: [{value: null, matchMode: FilterMatchMode.EQUALS}]},
            contributions_legal_entities: {operator: FilterOperator.AND, constraints: [{value: null, matchMode: FilterMatchMode.EQUALS}]},
            equity_on_balance_sheet: {operator: FilterOperator.AND, constraints: [{value: null, matchMode: FilterMatchMode.EQUALS}]},
            excess_of_income_tax: {operator: FilterOperator.AND, constraints: [{value: null, matchMode: FilterMatchMode.EQUALS}]},
        };
    };

    const loadLazyData = async () => {
        lazyParams.filters = filters.value;
        const {data} = await api.get(`/analytic/report/${route.params.id}/values/`, {
            params: {
                lazyEvent: JSON.stringify(lazyParams),
            },
        })
        records.value = data.results
        totalRecords.value = data.count
    }
    const onFilter = async () => {
        await loadLazyData();
    }

    const onPage = async (event: any) => {
        lazyParams = event;
        await loadLazyData()
    }
    const onSort = async (event: any) => {
        lazyParams = event;
        await loadLazyData();

    }
    return {
        filters,
        isLoading,
        first,
        totalRecords,
        lazyParams,
        records,
        initFilters,
        loadLazyData,
        onFilter,
        onPage,
        onSort,
    }
}
