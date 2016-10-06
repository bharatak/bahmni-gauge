{
  "name": "${orderSet.name}",
  "description": "${orderSet.description}",
  "operator": "${orderSet.operator}",
  "orderSetMembers": [
    <#list orderSet.orderSetMembers as member>
    {
      "orderType": {
        "uuid": "8189b409-3f10-11e4-adec-0800271c1b75"
      },
      "orderTemplate": "{\"drug\":{\"name\":\"${member.drugName}\",\"uuid\":\"${member.drugUuid}\"},\"dosingInstructions\":{\"dose\":${member.dose},\"doseUnits\":\"${member.doseUnit}\",\"frequency\":\"${member.frequency}\",\"route\":\"${member.route}\"},\"administrationInstructions\":\"${member.instruction}\",\"duration\":${member.duration},\"durationUnits\":\"Day(s)\",\"additionalInstructions\":\"Inst1\"}",
      "concept": {
        "display": "${member.conceptName}",
        "uuid": "${member.conceptUuid}"
      }
    }<#sep>,
    </#list>
  ]
}