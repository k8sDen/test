export interface ReportTableRecord {
    id: number
    title: string
    actives: number | null
    loan_portfolio_total: number | null
    reverse_repo_operations: number | null
    late_payments_7_sum: number | null
    late_payments_7_portfolio: number | null
    late_payments_30_sum: number | null
    late_payments_30_portfolio: number | null
    late_payments_90_sum: number | null
    late_payments_90_portfolio: number | null
    amount_remuneration: number | null
    provision_requirements: number | null
    liabilities: number | null
    contributions_individuals: number | null
    contributions_legal_entities: number | null
    equity_on_balance_sheet: number | null
    excess_of_income_tax: number | null
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
    first?: number;      // Индекс первой записи
    rows?: number;       // Количество записей на странице
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

export interface Report {
    id: number
    title: string
    date: Date
    code: string
    unit: string
    timestamp: Date
}
