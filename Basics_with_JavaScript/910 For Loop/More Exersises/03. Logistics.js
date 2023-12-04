function vladi(array) {
  let goodsQty = Number(array[0]);
  let totalGoods = 0;
  let busGoods = 0;
  let truckGoods = 0;
  let trainGoods = 0;
  let pricePerTon = 0;
  let average = 0;
  let totalPrice = 0;

  for (let i = 1; i <= goodsQty; i++) {
    let goods = Number(array[i]);

    if (goods <= 3) {
      pricePerTon = 200;
      busGoods += goods;
    } else if (goods >= 4 && goods <= 11) {
      pricePerTon = 175;
      truckGoods += goods;
    } else if (goods >= 12) {
      pricePerTon = 120;
      trainGoods += goods;
    }
  }
  totalGoods = busGoods + truckGoods + trainGoods;
  totalPrice = busGoods * 200 + truckGoods * 175 + trainGoods * 120;
  average = (totalPrice / totalGoods).toFixed(2);

  busGoods = ((100 * busGoods) / totalGoods).toFixed(2);
  truckGoods = ((100 * truckGoods) / totalGoods).toFixed(2);
  trainGoods = ((100 * trainGoods) / totalGoods).toFixed(2);
  console.log(average);
  console.log(`${busGoods}%`);
  console.log(`${truckGoods}%`);
  console.log(`${trainGoods}%`);
}

vladi(["4", "1", "5", "16", "3"]);
vladi(["5", "2", "10", "20", "1","7"]);
