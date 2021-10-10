/*
  Sequences : 2, 8, 24, 10, 40, 120, 106

  Problem : 
  Number init : 22
  steps : 6
  number final : ?

*/
interface IResult {
    totalSteps: number;
    lineNumbers: number[];
    numberFinal: number;
}

enum problem1 {
    numberInit = 25,
    steps = 12
}


function calculate(): IResult {
    let totalSteps: number = 0;
    let lineNumbers: number[] = [problem1.numberInit];
    let numberFinal: number ;
    const RULES = [{ number: 4, action : 'times'}, { number: 3, action : 'times'},
                    { number: 14, action : 'substract'}]
    let contRules = 0;
    let nInit = problem1.numberInit;
    for (let i: number = 1; i < problem1.steps; i++) {
        const { number, action } = RULES[contRules];

        if(action === 'times'){
            nInit *= number;
        }
        else if(action === 'substract'){
            nInit -= number;
        }
        lineNumbers.push(nInit);
        contRules++;
        if(contRules == RULES.length){
            contRules = 0;
        }
    }
    numberFinal = lineNumbers[lineNumbers.length];

    return { totalSteps, lineNumbers, numberFinal}
}

let result:IResult = calculate();

console.log(result.lineNumbers);