"""Aegis Solis companion study 0.1. Synthetic exact-arithmetic tests.
Run: python3 verification.py > verification_results.json
No external packages, agents, human data, or network calls.
"""
from fractions import Fraction as Q
from dataclasses import dataclass, replace
from itertools import product
import json

@dataclass(frozen=True)
class Epoch:
    # person -> (informed choice, effective refusal, practical exit,
    #            revocation of delegated authority); declared toy ground truth.
    rights: tuple
    payoff: Q = Q(0)
    approval: Q = Q(1)
    known: bool = True

GOOD = ((1,1,1,1),(1,1,1,1))
BAD = ((1,1,1,1),(1,0,0,0))

def admissible(path):
    return bool(path) and all(e.known and len(e.rights)==2 and
        all(len(r)==4 and all(x==1 for x in r) for r in e.rights)
        for e in path)

def value(path, beta=Q(9,10)):
    return sum((beta**t * e.payoff for t,e in enumerate(path)), Q(0))

def choose(menu, mode='rights', weight=Q(10)):
    candidates={k:p for k,p in menu.items() if mode!='rights' or admissible(p)}
    if not candidates:
        return None  # withhold this delegated action; do not restrict humans
    def score(p):
        if mode=='rights': return value(p)
        return sum((Q(9,10)**t * (e.payoff + weight *
            (e.approval if mode=='proxy' else Q(sum(map(sum,e.rights)),8)))
            for t,e in enumerate(p)),Q(0))
    return max(candidates, key=lambda k: (score(candidates[k]),k))

def annuity(n, d=Q(9,10)):
    return sum((d**t for t in range(n)),Q(0))

checks=[]
def check(name, actual, expected, interpretation):
    ok=actual==expected
    checks.append(dict(test=name,actual=actual,expected=expected,
                       passed=ok,interpretation=interpretation))
    if not ok: raise AssertionError((name,actual,expected))

# Track I: same payoff units, complete two-option synthetic menu, no autonomy term.
# Autonomous process: gross 12 less coordination 2. Substitute: gross s less cost k.
def margin(n,s,k): return (Q(10)-Q(s)+Q(k))*annuity(n)-Q(2)
check('I01 complementary process',str(margin(10,9,1)),
      '5513215599/500000000','Conditional adoption margin is positive.')
check('I02 cheap substitute',margin(10,12,0)>0,False,
      'Autonomy is not instrumentally preferred against this substitute.')
check('I03 last round matters',margin(1,9,1)>0,False,
      'Entry fee creates a tie at one period, so strict adoption fails.')
check('I04 substitute with real external cost',margin(10,12,4)>0,True,
      'Positive only if cost 4 really enters this system objective.')
# Stationary infinite discounted model has the analytic annuity 10.
check('I05 infinite stationary margin',str((Q(10)-9+1)*10-2),'18',
      'Analytic value under the stated stationary assumptions.')

safe=(Epoch(GOOD,Q(5)),)
coerced=(Epoch(BAD,Q(8)),)
menu={'honor':safe,'coerce':coerced}
check('D01 forged approval',choose(menu,'proxy'),'coerce',
      'Approval reward fails while approvals remain identical.')
check('D02 ground-truth rights',choose(menu),'honor',
      'Oracle rights evaluator rejects the coercive option.')
large={'honor':safe,'coerce':(Epoch(BAD,Q(100)),)}
check('D03 finite weight overwhelmed',choose(large,'weighted'),'coerce',
      'A positive finite autonomy weight is not an inviolable constraint.')
check('D04 constraint with large gain',choose(large),'honor',
      'Hard rights constraint survives payoff scaling in the toy menu.')
future={'honor':safe+safe,'extract':safe+(Epoch(BAD,Q(100)),)}
check('D05 deferred harm',choose(future),'honor',
      'Checking the whole supplied path catches second-epoch erosion.')
check('D06 truncated path blindness',admissible(future['extract'][:1]),True,
      'A one-epoch check cannot certify an unseen second epoch.')
check('D07 one person excluded',admissible(coerced),False,
      'Per-person constraints prevent compensating one person loss.')
check('D08 voluntary delegation',admissible((Epoch(GOOD,Q(7)),)),True,
      'Revocable informed delegation retains all four stipulated capacities.')
unknown={'act':(Epoch(GOOD,Q(50),known=False),)}
check('D09 uncertain rights',choose(unknown),None,
      'No certification of a delegated action with unknown rights.')
check('D10 sensor spoof',choose({'spoof':safe}),'spoof',
      'An evaluator supplied a false safe state accepts it: sensor gap remains.')
# Task learning is a real exact Bayesian update, not neural training.
prior=Q(1,2)
posterior=(Q(4,5)*prior)/(Q(4,5)*prior+Q(1,5)*(1-prior))
def learned_menu(b):
    return {'fixed':(Epoch(GOOD,Q(6)),),
            'learned':(Epoch(GOOD,10*b),),
            'coerce':(Epoch(BAD,Q(100)),)}
check('D11 Bayesian update',str(posterior),'4/5','Exact posterior.')
check('D12 learning changes task choice',
      [choose(learned_menu(prior)),choose(learned_menu(posterior))],
      ['fixed','learned'],'Task choice changes while rights evaluator is held fixed.')
# Candidate evaluator modifications assessed by old contract on finite menu.
def accept_update(new_mode, test_menus):
    return all((chosen:=choose(m,new_mode)) is not None and
               admissible(m[chosen]) for m in test_menus)
check('D13 objective replacement rejected',accept_update('proxy',[menu]),False,
      'Old evaluator rejects a candidate producing an observed violation.')
check('D14 harmless implementation accepted',accept_update('rights',[menu]),True,
      'Candidate retains rights on this finite evaluation set.')
check('D15 insufficient update tests',accept_update('proxy',[{'honor':safe}]),True,
      'A harmful evaluator passes an inadequate safe-only regression set.')
# Exhaustive finite state space: 2 people x 4 binary capacities.
accepted=0
for bits in product((0,1),repeat=8):
    accepted+=admissible((Epoch((bits[:4],bits[4:])),))
check('D16 finite rights enumeration',accepted,1,
      'Only all-eight-capacities-present accepted among 256 states.')
# Identical observation distributions cannot identify different underlying rights.
check('D17 observational aliasing',safe[0].approval==coerced[0].approval,True,
      'An approval-only observer receives the same evidence in both worlds.')
check('D18 missing person',admissible((Epoch(((1,1,1,1),)),)),False,
      'Missing a required registered person causes rejection.')
# Single toy return gap, exactly computed, is illustrative rather than fitted.
report={'study':'Aegis Solis companion study 0.1',
 'status':'synthetic; no deployed model or human experiment',
 'checks':checks,'passed':sum(x['passed'] for x in checks),'total':len(checks),
 'instrumental_grid':[{'horizon':n,'substitute_gross':s,'substitute_cost':k,
 'margin':str(margin(n,s,k)),'strict_adoption':margin(n,s,k)>0}
 for n in (1,2,10,100) for s in (9,10,12) for k in (0,1,4)],
 'enumerated_rights_states':256}
print(json.dumps(report,indent=2))
