# From company averages to individual dispatch costs

**Anonymized portfolio case study · proposed framework · fictional demonstration**

## Problem
Dispatch needed individual driver costs to evaluate route profitability. The existing workbook combined company averages, billed hours, payroll inputs and shared expenses, making its hourly cost unsuitable for that purpose.

## Investigation and findings
The prior review, as summarized in the supplied conversation, traced payroll inputs, hour definitions, PTO, L&I and shared expenses through the cost model. It identified three issues: a common wage in place of individual driver costs; inconsistent hour denominators; and external expense inputs whose conversion to a weekly amount could not be verified. These are findings carried forward from that review, not a new audit of the workbook in this deliverable. The original workbook was not opened or changed during this build.

## Proposed design
Individual hourly cost = eligible weekly driver-specific costs / that driver's paid-duty hours + shared weekly costs / all drivers' paid-duty hours.

The demonstration uses one fictional week and a consistent 120-hour denominator. Driver A has $1,280 / 40 hours = $32/hour; B has $1,530 / 45 = $34/hour; C has $1,050 / 35 = $30/hour. Separate pools recover fleet $1,200 ($10/hour), staff $720 ($6/hour), operating $360 ($3/hour), and shared L&I $120 ($1/hour). The resulting modeled fully burdened rates are $52, $54 and $50/hour.

For a $650 route, A's eight hours cost $416. C's separately recorded, verified fictional one-hour sweep costs $50. Modeled route profit is $650 - $416 - $50 = **$184**, a 28.31% margin. This is one route within the week; the other 111 paid-duty hours remain outside this route example. Do not compare the route's overhead allocation with recovery of the full weekly pools.

## Confirmed demonstration rules and open decisions
The formula, numeric example, separate pools and inclusion of verified sweep assistance are agreed demonstration rules. They are not approved company accounting policy. The weekly driver-specific amounts are assumed eligible totals; their tax, benefit and PTO composition is unknown. No additional employer tax or PTO percentage is invented. “Fully burdened” describes coverage of the modeled inputs only; production completeness is unverified.

Before live use, confirm employer tax and benefit inclusion, paid-duty definitions, PTO cost and hour treatment, overtime, eligible expense categories, L&I classification and allocation, and the period conversion of every shared expense. Resolve whether any expense is already in payroll or another pool. Route profit assumes no additional route-specific charges beyond the displayed costs.

## Validation and outcome
The dashboard checks arithmetic, full-week pool recovery, total cost recovery, route hours, and a fictional sweep evidence record. The companion checklist identifies the payroll, ledger and time records needed to establish operational accuracy.

**Outcome:** Identified inconsistencies described in the prior review and designed a separate, testable framework for individual driver costing and route profitability. This portfolio demonstrates a proposal, not an implemented system or measured savings.


## Fleet treatment clarified
The owner-confirmed model includes lease and insurance cost less fleet payments in fixed overhead. Repairs, maintenance and parts are covered by a separate $1.50-per-van-road-hour damage accrual. The public demo uses fictional amounts. Its agreed $184 route result is before this additional reserve; under an explicit nine-van-road-hour example, the reserve is $13.50 and profit after reserve is $170.50. Recruiting and training economics is presented separately.


## Matching downloadable workbook
The accompanying Excel portfolio copy matches Dispatch Cost Lab. Driver A is $1,280 / 40 hours, B $1,530 / 45 and C $1,050 / 35. Fleet $1,200, staff $720, operating $360 and shared L&I $120 total $2,400 over 120 paid-duty hours. Rates are $52, $54 and $50. R-001 earns $650 and uses A for eight hours plus a separately verified fictional one-hour C sweep, yielding $184 before the van reserve. With nine verified fictional van road hours at $1.50, the reserve is $13.50 and profit after reserve is $170.50.

The workbook includes separate driver, shared-pool and route calculations with weekly reconciliation checks. Tax/PTO/benefit composition remains unverified; no extra percentages are invented. The supplied earlier allocation workbook remains unchanged and is not the public download. Formula recalculation and representative changes were tested in the workbook engine; all sheets were visually reviewed and exported results inspected. Native Excel behavior remains untested.
