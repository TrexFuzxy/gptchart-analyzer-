import { useState } from 'react';
import axios from 'axios';

export default function Backtest() {
  const [csv, setCsv] = useState(null);
  const [result, setResult] = useState(null);
  const [entry, setEntry] = useState("");
  const [sl, setSl] = useState("");
  const [tp, setTp] = useState("");

  const handleSubmit = async () => {
    const formData = new FormData();
    formData.append("file", csv);
    formData.append("entry", entry);
    formData.append("stop_loss", sl);
    formData.append("take_profit", tp);

    const { data } = await axios.post("http://localhost:5000/api/backtest", formData);
    setResult(data);
  };

  return (
    <div className="p-6 max-w-xl mx-auto">
      <h1 className="text-2xl font-bold mb-4">📈 Backtest Strategy</h1>
      <input type="file" accept=".csv" onChange={(e) => setCsv(e.target.files[0])} className="mb-2" />
      <input type="text" placeholder="Entry Price" onChange={(e) => setEntry(e.target.value)} className="mb-2 block" />
      <input type="text" placeholder="Stop Loss" onChange={(e) => setSl(e.target.value)} className="mb-2 block" />
      <input type="text" placeholder="Take Profit" onChange={(e) => setTp(e.target.value)} className="mb-4 block" />
      <button onClick={handleSubmit} className="bg-blue-500 text-white px-4 py-2 rounded">Run Backtest</button>
      {result && <div className="mt-4">
        <p>Total Trades: {result.total}</p>
        <p>Wins: {result.wins}</p>
        <p>Losses: {result.losses}</p>
        <p>Winrate: {result.winrate}%</p>
      </div>}
    </div>
  );
}