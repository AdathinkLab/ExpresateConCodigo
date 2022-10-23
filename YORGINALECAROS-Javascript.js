const absoluteValue = (num) => {
    const newNumber = num < 0 ? -num : num;

    console.log(`The absolute value of ${num} is ${newNumber}`);
}

absoluteValue(5);
absoluteValue(-0.5);
absoluteValue(-4);
absoluteValue(3.1);
absoluteValue(0);
absoluteValue(-8.9);