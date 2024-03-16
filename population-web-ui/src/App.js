import React from "react";


function CityList(props) {
  const cities = props.cities || [];
  return (
    <div className="card">
      <div className="card-header">Cities</div>
      <div className="card-body">
        <table className="table">
          <thead>
            <tr>
              <th>S.No</th>
              <th>Name</th>
              <th>Country</th>
              <th>Continent</th>
              <th>Population</th>
            </tr>
          </thead>
          <tbody>
            {cities.map((city, idx) => (
              <tr key={city.name}>
                <td>{idx + 1}</td>
                <td>{city.name}</td>
                <td>{city.country}</td>
                <td>{city.continent}</td>
                <td>{city.population}</td>
              </tr>
            ))}
          </tbody>
        </table>
      </div>
    </div>
  )
}


function App() {

  const [cities, setCities] = React.useState([]);

  React.useEffect(() => {
    fetch('http://localhost:5000/api/cities')
      .then(response => response.json())
      .then(data => setCities(data));
  }, [])

  return (
    <div className="container">
      <div className="display-1">
        Population
      </div>
      <hr />
      <CityList cities={cities} />
    </div>
  );
}

export default App;
