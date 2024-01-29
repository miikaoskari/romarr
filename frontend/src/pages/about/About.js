import { Card, Grid } from '../../components';
import React from 'react';

const About = () => {
  return (
    <div className='bg-gray-900 rounded-3xl '>
      <Grid>
        <Card header={"Disk (C:/)"} content={"280 GB free of 464 GB"}>
          <h1>1</h1>
        </Card>
        <Card header={"Disk (C:/)"} content={"280 GB free of 464 GB"}>
          <h1>2</h1>
        </Card>
        <Card header={"Disk (C:/)"} content={"280 GB free of 464 GB"}>
          <h1>3</h1>
        </Card>
        <Card header={"Disk (C:/)"} content={"280 GB free of 464 GB"}>
          <h1>4</h1>
        </Card>
        <Card header={"Disk (C:/)"} content={"280 GB free of 464 GB"}>
          <h1>5</h1>
        </Card>
        <Card header={"Disk (C:/)"} content={"280 GB free of 464 GB"}>
          <h1>6</h1>
        </Card>
      </Grid>
    </div>
  );
};

export default About;
