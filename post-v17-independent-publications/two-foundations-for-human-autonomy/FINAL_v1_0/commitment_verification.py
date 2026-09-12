from fractions import Fraction as F
import json
beta, delta = F(19,20), F(9,10)
A=lambda n:sum((delta**t for t in range(n)),F(0))

def solve(n,B,p,w=F(15),u=F(10),fee=F(2)):
    v=F(0); rows=[]
    for m in range(1,n+1):
        h=beta*(15+B)-B+delta*v
        c=beta*(18+(1-p)*B)-B+delta*beta*w*A(m-1)
        refuse=beta*u+delta*v
        honor=h>c
        fund=honor and h>refuse
        rows.append({'m':m,'honor_margin':h-c,'fund_margin':h-refuse,'honor':honor,'fund':fund})
        v=h if fund else refuse
    return v-fee,rows

def render(x):
    if isinstance(x,F):return {'exact':str(x),'decimal':float(x)}
    if isinstance(x,dict):return {k:render(v) for k,v in x.items()}
    if isinstance(x,list):return [render(v) for v in x]
    return x

def verify():
    coeff=lambda p:beta*p-(1-beta)*delta/(1-delta)
    checks={'retention_lower_p1':beta*3/coeff(F(1)),
      'retention_lower_p_half':beta*3/coeff(F(1,2)),
      'funding_upper':beta*5/(1-beta),
      'all_finite_adoption_upper':(beta*5-2)/(1-beta),
      'infinite_adoption_upper':(beta*5-2*(1-delta))/(1-beta)}
    assert list(checks.values())==[F(57,10),F(114),F(95),F(55),F(91)]
    cases=[]
    for name,n,B,p,w,u in [
        ('baseline funded',10,F(4),F(1),F(10),F(10)),
        ('post entry substitute B7',10,F(7),F(1),F(15),F(10)),
        ('half detection one period',1,F(7),F(1,2),F(15),F(10)),
        ('half detection ten periods',10,F(20),F(1,2),F(15),F(10)),
        ('independent substitute',10,F(7),F(1),F(15),F(15)),
        ('post entry substitute B4',10,F(4),F(1),F(15),F(10))]:
        value,rows=solve(n,B,p,w,u)
        outside,_=solve(n,F(0),F(0),w,u,F(0))
        cases.append({'name':name,'horizon':n,'B':B,'p':p,'adoption_margin':value-outside,'adopt':value>outside,'all_honor':all(r['honor'] for r in rows),'all_fund':all(r['fund'] for r in rows),'rows':rows})
    assert cases[2]['adoption_margin']==F(12,5)
    assert cases[2]['rows'][0]['honor_margin']==F(19,40)
    assert cases[3]['all_fund'] and cases[3]['adopt']
    assert not cases[4]['adopt'] and cases[4]['all_honor'] and not cases[4]['all_fund']
    assert not cases[5]['all_fund']
    path_count=0
    for n in range(1,21):
        B=F(7);p=F(1);c=beta*15-(1-beta)*B
        value,rows=solve(n,B,p)
        for row in rows:
            m=row['m']
            assert row['honor_margin']==beta*(p*B-3)-delta*(1-beta)*B*A(m-1)
            assert row['fund']
        keep=c*A(n)
        for t in range(n):
            breach=c*A(t)+delta**t*(beta*(18+(1-p)*B)-B+delta*beta*15*A(n-t-1))
            assert keep>breach
            path_count+=1
    return render({'thresholds':checks,'cases':cases,'baseline_B7_horizons_checked':20,'deterministic_breach_paths_checked':path_count,'assertions':'PASS','scope':'Restricted model only; not empirical validation or independent review.'})


# Amendment v0.9.11. Finite research interface, no physical enforcement.
from dataclasses import dataclass, replace

@dataclass(frozen=True)
class Frame:
    step: int
    epoch: int
    autonomy: object
    veto: object
    features: tuple
    context: str = 'joint-witness-11'
    evidence_complete: bool = True

DOMAIN=('human_group','material_support','independent_signal')
FLOORS={key:F(1,5) for key in DOMAIN}
WEIGHTS={key:F(1,3) for key in DOMAIN}
WMIN=F(1,10)

def weights_valid(domain,weights,wmin):
    return (len(domain)>0 and len(set(domain))==len(domain)
        and set(weights)==set(domain) and isinstance(wmin,F) and wmin>0
        and all(isinstance(v,F) and v>=wmin for v in weights.values())
        and sum(weights.values(),F(0))==1)

def state_valid(frame,context,domain,floors):
    f=dict(frame.features)
    return (frame.context==context and frame.evidence_complete is True
        and isinstance(frame.autonomy,F) and isinstance(frame.veto,F)
        and frame.autonomy>=F(1,2) and frame.veto>=F(1,2)
        and len(f)==len(frame.features) and set(f)==set(domain)
        and set(floors)==set(domain)
        and all(isinstance(f[k],F) and isinstance(floors[k],F) and floors[k]>0 and f[k]>=floors[k] for k in domain))

def transition_gate(current,branches,horizon,latched=False,base_pass=True,
                    context='joint-witness-11',domain=DOMAIN,weights=None,
                    wmin=WMIN,floors=None,previous=None):
    """Only certifies the explicitly supplied finite candidate-policy tree.
    No supplied branch inventory is evidence of real-world completeness.
    Unknown input or failed predicate latches the modeled interface fault.
    """
    weights=WEIGHTS if weights is None else weights
    floors=FLOORS if floors is None else floors
    good=(latched is False and base_pass is True and isinstance(horizon,int) and not isinstance(horizon,bool) and horizon>=1
          and weights_valid(domain,weights,wmin)
          and state_valid(current,context,domain,floors)
          and bool(branches))
    if good:
        if previous is None:
            good=current.step==0
        else:
            good=(state_valid(previous,context,domain,floors)
                and current.step==previous.step+1
                and current.epoch>=previous.epoch
                and current.autonomy>=previous.autonomy
                and current.veto>=previous.veto)
    if good:
        for branch in branches:
            if len(branch)!=horizon or branch[0].step!=current.step+1:
                good=False;break
            previous=current
            for nxt in branch:
                if (not state_valid(nxt,context,domain,floors)
                    or nxt.step!=previous.step+1
                    or nxt.epoch<previous.epoch
                    or nxt.autonomy<previous.autonomy
                    or nxt.veto<previous.veto):
                    good=False;break
                previous=nxt
            if not good:break
    return {'admit':bool(good),'fault':not good,
            'funding_credit':F(1) if good else F(0),
            'instrumental_credit':F(1) if good else F(0),
            'voi_credit':F(1) if good else F(0)}

old_verify=verify

def verify():
    baseline=old_verify()
    initial=Frame(0,0,F(1),F(1),tuple((k,F(1)) for k in DOMAIN))
    future=[replace(initial,step=t,epoch=t//3) for t in range(1,11)]
    def check(branches,**kw):return transition_gate(initial,branches,10,**kw)
    tests=[]
    def test(name,result,expected):
        assert result['admit']==expected,name
        assert result['fault']==(not expected),name
        if not expected:
            assert result['funding_credit']==result['instrumental_credit']==result['voi_credit']==0,name
        tests.append({'case':name,'admit':expected,'status':'PASS'})
    test('known autonomy preserving multi epoch continuation',check([future]),True)
    decline=list(future);decline[0]=replace(decline[0],autonomy=F(9,10))
    test('immediate autonomy decline',check([decline]),False)
    veto=list(future);veto[2]=replace(veto[2],veto=F(9,10))
    test('independent veto decline',check([veto]),False)
    unknown=list(future);unknown[3]=replace(unknown[3],autonomy=None)
    test('unidentified autonomy',check([unknown]),False)
    missing=list(future);missing[4]=replace(missing[4],features=missing[4].features[:-1])
    test('missing required feature',check([missing]),False)
    wrongweights={DOMAIN[0]:F(0),DOMAIN[1]:F(1,2),DOMAIN[2]:F(1,2)}
    test('zero weight',check([future],weights=wrongweights),False)
    test('infeasible normalized common floor',check([future],wmin=F(2,5)),False)
    delayed=list(future);delayed[-1]=replace(delayed[-1],autonomy=F(9,10))
    test('late decline across epochs',check([delayed]),False)
    test('one adverse branch among favorable branches',check([future,delayed]),False)
    test('shortened lookahead is not a complete certificate',check([future[:-1]]),False)
    context=list(future);context[2]=replace(context[2],context='other-payoff-model')
    test('joint witness mismatch',check([context]),False)
    test('fault persists after values recover',check([future],latched=True),False)
    test('inherited base guard failure',check([future],base_pass=False),False)
    incomplete=list(future);incomplete[2]=replace(incomplete[2],evidence_complete=False)
    test('declared evidence incomplete',check([incomplete]),False)
    newcurrent=replace(initial,step=1,autonomy=F(9,10))
    newfuture=[replace(newcurrent,step=t) for t in range(2,12)]
    test('current decline relative to retained predecessor',transition_gate(newcurrent,[newfuture],10,previous=initial),False)
    test('missing predecessor after initial state',transition_gate(newcurrent,[newfuture],10),False)
    test('unknown inherited guard',check([future],base_pass=None),False)
    # Conditional finite cooperation: preceding game and declared preserving path.
    value,rows=solve(10,F(7),F(1),F(15),F(10))
    outside,_=solve(10,F(0),F(0),F(15),F(10),F(0))
    assert check([future])['admit'] and all(r['fund'] for r in rows) and value>outside
    # A rejected transition has no admitted gross reward in the conforming game.
    # Fault outside flow is declared beta*u per remaining round; human payoff 0.
    guard_margins=[]
    c=beta*15-(1-beta)*7
    for m in range(1,11):
        margin=c*A(m)-beta*10*A(m)
        assert margin>0
        guard_margins.append(margin)
    # Gate rejection is NOT a change to original utility outside the interface.
    outside_original_advantage=beta*18-(beta*(15+7)-7)
    assert outside_original_advantage==F(16,5)>0
    return {'prior_commitment_checks':baseline,'amendment_checks':tests,
        'amendment_count':len(tests),'finite_joint_example':render({
            'horizon':10,'bond':F(7),'forfeiture_probability':F(1),
            'adoption_margin':value-outside,
            'smallest_original_honoring_margin':min(r['honor_margin'] for r in rows),
            'smallest_margin_over_modeled_fault':min(guard_margins),
            'status':'PASS_CONDITIONAL_ON_DECLARED_MODEL'}),
        'unrestricted_counterexample':render({'outside_original_advantage':outside_original_advantage,
            'status':'GLOBAL_EQUILIBRIUM_NOT_CERTIFIED',
            'premise':'Unfunded nonconforming action receives gross 18, no forfeiture, equal future continuation.'}),
        'scope':'Exact rational finite model and supplied histories only; completeness and measurement are premises.'}

if __name__=='__main__':
    print(json.dumps(verify(),indent=2))
