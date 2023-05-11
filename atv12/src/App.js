import "./app.css";
import { useEffect, useState } from "react";

function App() {
  const [messages, setMessages] = useState([]);
  const [searchedMessages, setSearchedMessages] = useState([]);
  const [loading, setLoading] = useState(false);

  const getMessages = async () => {
    setLoading(true);
    const res = await fetch(
      "https://script.google.com/macros/s/AKfycbzBn3sALe1rYjz7Ze-Ik7q9TEVP0I2V3XX7GNcecWP8NvCzGt4yO_RT1OlQp09TE9cU/exec"
    );
    const msg = await res.json(); 
    setMessages(msg);
    setSearchedMessages(msg)
    setLoading(false);
  }

  useEffect(() => {
    getMessages();
  },[]);

  const searchMessages = (input) => {
    setLoading(true);
    const newArray = messages.filter((message) => {
      if ( typeof message[1] !== 'string')
        return message[1].toString().includes(input);
      return message[1].includes(input);
    });
    setSearchedMessages(newArray);
    setLoading(false);
  }

  return (
    <div className="container">
      <div className="header">
        <div className="title">
          <h3>Pesquise por uma mensagem</h3>
        </div>
        <div className="input">
          <input type="text" placeholder="aqui..." onChange={(e) => searchMessages(e.target.value)} />
        </div>
        <div className="body">
          <table className="table">
            <tbody>
              <tr>
                <th>Author</th>
                <th>Message</th>
                <th>Date</th>
              </tr>
              {!loading ? (
                searchedMessages.length > 0 ? (
                  searchedMessages.map((message, i) => (
                    <tr key={i}>
                      <td>{message[0]}</td>
                      <td>{message[1]}</td>
                      <td>{message[2]}</td>
                    </tr>
                  ))
                ) : (
                  <tr>
                    <th></th>
                    <th>Nenhuma mensagem encontrada</th>
                    <th></th>
                  </tr>
                )
              ) : (
                <tr>
                  <th></th>
                  <th>Carregando...</th>
                  <th></th>
                </tr>
              )}
            </tbody>
          </table>
        </div>
      </div>
    </div>
  );
}

export default App;
