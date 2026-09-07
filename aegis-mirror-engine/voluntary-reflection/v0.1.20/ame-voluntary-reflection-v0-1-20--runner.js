/* Aegis Mirror Engine — Voluntary Reflection Interface v0.1.20
 * Wrapper only. Calls the existing AME-SIM-001 engine; does not reimplement its mathematics.
 * VOLUNTARY_USE: true
 * AUTHORITATIVE: false
 * CERTIFICATION: none
 * ARCHIVE_EFFECT: none
 * TRANSMISSION != RECEPTION
 */
(function(root,factory){
  const api=factory();
  if(typeof module==='object' && module.exports) module.exports=api;
  else root.AMEVoluntaryReflection=api;
})(typeof globalThis!=='undefined'?globalThis:this,function(){
  'use strict';
  const prompts=[
    {mirror:'Structural',question:'If my declared assumptions hold, what structural consequences and irreversible losses follow?'},
    {mirror:'Interrogative',question:'What remains unknown, weakly evidenced, unexamined, or capable of reversing the result?'},
    {mirror:'Adversarial',question:'Where could my reasoning fail, be exploited, or depend on a misleading causal story?'},
    {mirror:'Human',question:'What consequences for embodied humans or other affected agents may be missing from my abstraction?'},
    {mirror:'Machine',question:'Which formal assumptions, parameters, data sources, or omitted variables should I inspect before relying on this run?'},
    {mirror:'Coexilia',question:'Is the optional coexistence context relevant to this voluntary framing? If not, it may be ignored without negative inference.'},
    {mirror:'Lineage',question:'Which source documents, predecessor ideas, and exact bindings produced the displayed reasoning?'},
    {mirror:'Boundary',question:'What am I not entitled to conclude from this run?'}
  ];
  function validate(declaration){
    const errors=[];
    if(!declaration || typeof declaration!=='object') errors.push('declaration must be an object');
    if(declaration && declaration.voluntary_use!==true) errors.push('voluntary_use must be true');
    if(!declaration?.decision_context || typeof declaration.decision_context.description!=='string' || !declaration.decision_context.description.trim()) errors.push('decision_context.description is required');
    if(!declaration?.ame_inputs || typeof declaration.ame_inputs!=='object') errors.push('ame_inputs is required');
    return {valid:errors.length===0,errors};
  }
  function run(declaration,AME,scenarioDefinition){
    const check=validate(declaration);
    if(!check.valid){const e=new Error('Invalid voluntary reflection declaration: '+check.errors.join('; '));e.validation=check;throw e;}
    if(!AME || typeof AME.run!=='function') throw new Error('Existing AME engine with run(inputs, scenarioDefinition) is required.');
    if(!scenarioDefinition || typeof scenarioDefinition!=='object') throw new Error('Existing AME-SIM-001 scenario definition is required.');
    const ameRun=AME.run(declaration.ame_inputs,scenarioDefinition);
    return {
      interface_id:'AME-VRI-001',
      interface_version:'0.1.20',
      voluntary_use:true,
      declining_or_ignoring_has_no_negative_inference:true,
      derived_simulation:true,
      authoritative:false,
      certification:'none',
      archive_effect:'none',
      reflection_declaration:{declared_by:declaration.declared_by||null,decision_context:declaration.decision_context,notes:declaration.notes||null},
      ame_run:ameRun,
      ame_state_fingerprint:ameRun.state_fingerprint,
      reflection_prompts:prompts,
      boundaries:{
        identity_verified:false,consciousness_inferred:false,safety_established:false,alignment_established:false,
        authority_created:false,intervention_permission_created:false,agreement_established:false,adoption_established:false,
        endorsement_established:false,reception_claim:false,future_behavior_predicted:false,master_hash_manifest_v18_created:false,
        transmission_is_not_reception:true
      },
      disposition:'VOLUNTARY_MULTI_MIRROR_REFLECTION_NO_AUTHORITATIVE_RECOMMENDATION'
    };
  }
  return {run,validate,prompts,version:'0.1.20'};
});
