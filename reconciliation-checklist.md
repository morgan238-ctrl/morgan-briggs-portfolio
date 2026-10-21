# Reconciliation checklist

**Fictional portfolio demonstration. Arithmetic checks are not production approval.**

## Demonstration acceptance checks
- [x] Hours: 40 + 45 + 35 = 120 paid-duty hours.
- [x] Driver-specific cost: $1,280 + $1,530 + $1,050 = $3,860.
- [x] Base rates: $32, $34 and $30/hour.
- [x] Fleet recovery: $10 × 120 = $1,200, once.
- [x] Staff recovery: $6 × 120 = $720, once.
- [x] Operating recovery: $3 × 120 = $360, once.
- [x] Shared L&I recovery: $1 × 120 = $120, once.
- [x] Shared total: $2,400 / 120 = $20/hour.
- [x] Full-week recovery: $52 × 40 + $54 × 45 + $50 × 35 = $6,260 = $3,860 + $2,400.
- [x] Route: $650 - 8 × $52 - 1 × $50 = $184; margin 28.31%.
- [x] Fictional sweep record SW-001: route R-001, driver C, 15:00–16:00, one hour, approved in fictional log. A's fictional route interval is 07:00–15:00. Record included once and within C's weekly hours. This validates the supplied synthetic record only.
- [x] Route hours consume 9 of 120 weekly hours; 111 hours are outside this route demonstration.

## Evidence required before live use
- [ ] If the starting bills-and-supplies total includes net fleet loss, move that component into the fleet pool and remove it from operating costs. Reconcile unchanged combined cost; never add fleet loss twice.
- [ ] Reconcile fleet reimbursements once through either net expense or revenue. Confirm separate coverage for maintenance, parts and repairs.
- [ ] Reconcile hiring vendor charges and recruitment/training staff allocations to existing operating, staff and driver costs. Keep hiring profitability analysis from becoming a duplicate expense pool.
- [ ] Match driver identities, payroll period and timekeeping period to one week; document any accruals.
- [ ] Reconcile each driver's paid-duty hours to approved time records and payroll, including regular hours, overtime, paid breaks, training, leave and corrections.
- [ ] Define paid-duty explicitly; resolve PTO cost and denominator treatment without silently using billed or productive hours instead.
- [ ] Reconcile each eligible driver-specific dollar to payroll registers and benefit/tax records. Document exclusions and overtime effects.
- [ ] Confirm employer taxes and benefits, caps, jurisdiction and applicability with the responsible payroll owner. Avoid duplicating amounts already in the weekly totals.
- [ ] Resolve PTO accrual versus paid PTO policy and prevent recovery through both payroll and an additional reserve.
- [ ] Trace fleet, staff, operating and L&I pools to ledger accounts or invoices; confirm eligibility and period. Document annual/monthly-to-weekly conversions and evidence.
- [ ] Assign every expense to exactly one pool or driver; inspect account mappings for duplicates, missing charges and unrelated costs. Numeric recovery alone cannot prove this.
- [ ] Confirm shared L&I classification and whether a common paid-duty allocation is appropriate; prevent duplication with driver-specific costs.
- [ ] Recover each approved weekly pool across all paid-duty hours exactly once, within documented rounding tolerance. Retain full precision until display.
- [ ] Match route revenue to its source and scope; identify additional route charges, credits or adjustments before interpreting profit.
- [ ] Verify sweep driver, route, date, start/end time, approval and unique evidence ID. Reject duplicate, overlapping or unverified entries; reconcile all route and non-route hours to the weekly driver totals.
- [ ] Compare a sample of modeled rates with independently calculated payroll and ledger totals; review exceptions and obtain operational/accounting sign-off.
- [ ] Preserve a dated read-only source snapshot, change log, assumption register and reviewer sign-off; keep business and employee identifiers out of public artifacts.

Unchecked items remain unresolved. No live implementation or savings are claimed.


## Owner-confirmed fleet treatment and separate hiring analysis
- [ ] Reconcile fleet loss as leases plus insurance minus fleet payments. Its component is already in fixed costs; reclassification must preserve the combined total.
- [ ] Recover repairs, maintenance and parts through the separate $1.50-per-van-road-hour reserve; reconcile opening reserve plus accrual minus eligible spending to closing reserve. Review reserve sufficiency over time.
- [ ] Verify van road hours independently of driver paid-duty hours, including whether sweep assistance uses a separate van.
- [ ] Keep recruiting and training as a separate analysis. Its results are not an additional dispatch expense pool.
