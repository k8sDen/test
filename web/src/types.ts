export interface ReportTableRecord {
    id: number
    bank: string
    actives: number | null
    loan_portfolio_total: number | null
    loan_portfolio_including_reverse_repo_operations: number | null
    from_it_loans_with_late_payments_over_7_days_sum: number | null
    from_it_loans_with_late_payments_over_7_days_share_in_the_loan_portfolio: number | null
    from_it_loans_with_late_payments_over_30_days_sum: number | null
    from_it_loans_with_late_payments_over_30_days_share_in_the_loan_portfolio: number | null
    from_it_loans_with_late_payments_over_90_days_sum: number | null
    from_it_loans_with_late_payments_over_90_days_share_in_the_loan_portfolio: number | null
    amount_of_overdue_loans_including_overdue_remuneration: number | null
    provisions_formed_for_the_loan_portfolio_in_accordance_with_IFRS_requirements: number | null
    liabilities: number | null
    of_which_contributions_individuals: number | null
    of_which_contributions_legal_entities: number | null
    equity_on_balance_sheet: number | null
    excess_of_current_income_expenses_over_current_expenses_income_after_payment_of_income_tax: number | null
}

export interface FilterEvent {
    filters: {
        [field: string]: {
            value: any;
            matchMode: string;
        }
    };
    field: string;  // поле, по которому применяется фильтр
    value: any;    // значение фильтра
    matchMode: string; // режим сравнения (например, 'startsWith', 'contains', 'equals' и т.д.)
}

export interface LazyParams {
    first: number;      // Индекс первой записи
    rows: number;       // Количество записей на странице
    sortField?: string; // Поле для сортировки
    sortOrder?: number; // Порядок сортировки (1 для возрастания, -1 для убывания)
    filters?: {
        [field: string]: {
            value: any;   // Значение фильтра
            matchMode: string; // Режим сопоставления, например 'startsWith', 'contains', 'equals' и т.д.
        };
    };
    globalFilter?: any; // Глобальный фильтр
    multiSortMeta?: Array<{
        field: string;
        order: number;
    }>;
}
