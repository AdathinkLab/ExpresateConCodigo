var problem1;
(function (problem1) {
    problem1[problem1["numberInit"] = 25] = "numberInit";
    problem1[problem1["steps"] = 12] = "steps";
})(problem1 || (problem1 = {}));
function calculate() {
    var totalSteps = 0;
    var lineNumbers = [problem1.numberInit];
    var numberFinal;
    var RULES = [{ number: 4, action: 'times' }, { number: 3, action: 'times' },
        { number: 14, action: 'substract' }];
    var contRules = 0;
    var nInit = problem1.numberInit;
    for (var i = 1; i < problem1.steps; i++) {
        var _a = RULES[contRules], number = _a.number, action = _a.action;
        if (action === 'times') {
            nInit *= number;
        }
        else if (action === 'substract') {
            nInit -= number;
        }
        lineNumbers.push(nInit);
        contRules++;
        if (contRules == RULES.length) {
            contRules = 0;
        }
    }
    numberFinal = lineNumbers[lineNumbers.length];
    return { totalSteps: totalSteps, lineNumbers: lineNumbers, numberFinal: numberFinal };
}
var result = calculate();
console.log(result.lineNumbers);
