-- 1-actives
-- 3-loan_portfolio_total
-- 5-reverse_repo_operations
-- 8-late_payments_7_sum
-- 9-late_payments_7_portfolio
-- 11-late_payments_30_sum
-- 12-late_payments_30_portfolio
-- 14-late_payments_90_sum
-- 15-late_payments_90_portfolio
-- 16-amount_remuneration
-- 17-provision_requirements
-- 18-liabilities
-- 20-contributions_individuals
-- 21-contributions_legal_entities
-- 22-equity_on_balance_sheet
-- 23-excess_of_income_tax
create view app.public.analytic_indicator_value_view
            (id,
             report_bank_id,
             title,
             report_id,
             actives,
             loan_portfolio_total,
             reverse_repo_operations,
             late_payments_7_sum,
             late_payments_7_portfolio,
             late_payments_30_sum,
             late_payments_30_portfolio,
             late_payments_90_sum,
             late_payments_90_portfolio,
             amount_remuneration,
             provision_requirements,
             liabilities,
             contributions_individuals,
             contributions_legal_entities,
             equity_on_balance_sheet,
             excess_of_income_tax)
as
select ab.id,
       arb.id    as report_bank_id,
       ab.title,
       arb.report_id,
       (SELECT value
        FROM analytic_indicator_values
        WHERE ab.id = bank_id
          AND arb.report_id = report_id
          AND indicator_id = 1
        LIMIT 1) AS actives,
       (SELECT value
        FROM analytic_indicator_values
        WHERE ab.id = bank_id
          AND arb.report_id = report_id
          AND indicator_id = 3
        LIMIT 1) AS loan_portfolio_total,
       (SELECT value
        FROM analytic_indicator_values
        WHERE ab.id = bank_id
          AND arb.report_id = report_id
          AND indicator_id = 5
        LIMIT 1) AS reverse_repo_operations,
       (SELECT value
        FROM analytic_indicator_values
        WHERE ab.id = bank_id
          AND arb.report_id = report_id
          AND indicator_id = 8
        LIMIT 1) AS late_payments_7_sum,
       (SELECT value
        FROM analytic_indicator_values
        WHERE ab.id = bank_id
          AND arb.report_id = report_id
          AND indicator_id = 9
        LIMIT 1) AS late_payments_7_portfolio,
       (SELECT value
        FROM analytic_indicator_values
        WHERE ab.id = bank_id
          AND arb.report_id = report_id
          AND indicator_id = 11
        LIMIT 1) AS late_payments_30_sum,
       (SELECT value
        FROM analytic_indicator_values
        WHERE ab.id = bank_id
          AND arb.report_id = report_id
          AND indicator_id = 12
        LIMIT 1) AS late_payments_30_portfolio,
       (SELECT value
        FROM analytic_indicator_values
        WHERE ab.id = bank_id
          AND arb.report_id = report_id
          AND indicator_id = 14
        LIMIT 1) AS late_payments_90_sum,
       (SELECT value
        FROM analytic_indicator_values
        WHERE ab.id = bank_id
          AND arb.report_id = report_id
          AND indicator_id = 15
        LIMIT 1) AS late_payments_90_portfolio,
       (SELECT value
        FROM analytic_indicator_values
        WHERE ab.id = bank_id
          AND arb.report_id = report_id
          AND indicator_id = 16
        LIMIT 1) AS amount_remuneration,
       (SELECT value
        FROM analytic_indicator_values
        WHERE ab.id = bank_id
          AND arb.report_id = report_id
          AND indicator_id = 17
        LIMIT 1) AS provision_requirements,
       (SELECT value
        FROM analytic_indicator_values
        WHERE ab.id = bank_id
          AND arb.report_id = report_id
          AND indicator_id = 18
        LIMIT 1) AS liabilities,
       (SELECT value
        FROM analytic_indicator_values
        WHERE ab.id = bank_id
          AND arb.report_id = report_id
          AND indicator_id = 20
        LIMIT 1) AS contributions_individuals,
       (SELECT value
        FROM analytic_indicator_values
        WHERE ab.id = bank_id
          AND arb.report_id = report_id
          AND indicator_id = 21
        LIMIT 1) AS contributions_legal_entities,
       (SELECT value
        FROM analytic_indicator_values
        WHERE ab.id = bank_id
          AND arb.report_id = report_id
          AND indicator_id = 22
        LIMIT 1) AS equity_on_balance_sheet,
       (SELECT value
        FROM analytic_indicator_values
        WHERE ab.id = bank_id
          AND arb.report_id = report_id
          AND indicator_id = 23
        LIMIT 1) AS excess_of_income_tax
from app.public.analytic_report_banks as arb
         left join public.analytic_banks as ab on ab.id = arb.bank_id;

alter table app.public.analytic_indicator_value_view
    owner to superuser;

