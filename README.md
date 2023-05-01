# Hello Everyone !!! Welcome to RoastRoute !!! 
- brought to you by Team 19
![team19photo](https://user-images.githubusercontent.com/93873940/235373311-a15d9c1d-dbf8-4aaf-a7ac-b872006ef460.jpg)

## What is RoastRoute ? 
- RoastRoute is a Geographic Information System designed to provide a platform for coffee lovers to organize coffee dates, with features that follow state-of-the-art conventions, making it extremely usable and resposive.
![Screenshot 2023-04-30 at 7 13 56 PM](https://user-images.githubusercontent.com/93873940/235380410-9c7cddc7-0a3e-413f-99a2-2cba3bd2c1e8.png)



## Why RoastRoute?
- Roast Route lets you easily locate your favourite coffee shops through our coffee shops button
- Roast Route's find Coffee Dates feature allows you to quickly search for people like you that want to connect over a cup of coffee
- Roast Route has state-of-the-art path-finding algorithms implemented to help you get to your coffee date or your favourite coffee shop as soon as possible

## Basic Features
![Screenshot 2023-04-30 at 6 49 29 PM](https://user-images.githubusercontent.com/93873940/235379551-c2324437-7108-4c56-9260-173d60c3c44e.png)
![Screenshot 2023-04-30 at 6 49 42 PM](https://user-images.githubusercontent.com/93873940/235379555-aab1e1c7-43f0-48c4-b625-ad74b87a9d93.png)

## Search Bar
- A search bar supports search by text entry and pin placing
- Search bar supports auto-zooming feature 
- 3 search types: by Point of Interest, Street, Intersection

## Find nearest coffee shops
Using the GoogleMapsAPI, we query specifically coffee shops that are within a certain distance from the users pin and lets them easily see nearby coffee shops and their ratings.
![Screenshot 2023-04-30 at 6 56 19 PM](https://user-images.githubusercontent.com/93873940/235379802-c58105fb-1bd5-4c1b-9698-4a2aa72a8f87.png)

## Find coffee dates
Our team implemented a FASTAPI to allow our application to have users connect with other users on the map and communicate with them.
<img width="1289" alt="Screenshot 2023-04-30 at 6 58 59 PM" src="https://user-images.githubusercontent.com/93873940/235379904-063d3afc-5c31-416a-a0d5-033e0e3cc79b.png">

## Path Finding Algorithm
The team tried the implementation of both Dijkstra and A*. We eventually deicided to use Dijkstra for multi-destiation Dijkstra used for solving the travelling courier problem.
<table>
  <tbody>
    <tr>
      <td>Dijkstra</td>
      <td>A*</td>
    </tr>
    <tr>
      <td>Always guranteed to find optimal path as it considers all nodes in the graph reaching </td>
      <td>A* is computationally faster as it uses a underestimate heuristic (estimated travel time from neighbouring node to destination)</td>
    </tr>
  </tbody>
</table>

## Path finding results shown on map:
<img src="https://user-images.githubusercontent.com/93873940/235380204-91c5232f-735d-4b66-ae00-033cfc869c5a.png" alt="Screenshot">

## Path-finding results:
<table>
  <tbody>
    <tr>
      <td>Results</td>
      <td>Toronto</td>
      <td>London</td>
    </tr>
    <tr>
      <td>Travel Times</td>
      <td>
      <img src="https://user-images.githubusercontent.com/93873940/235380500-6d19364f-0b2b-4ddc-b294-27abc8defe40.png" alt="Screenshot">
      </td>
      <td>
<img src="https://user-images.githubusercontent.com/93873940/235380516-c0e17e65-4c51-4915-8c0c-72445dedfb0b.png" alt="Screenshot">
      </td>
    </tr>
    <tr>
      <td>Computation Times</td>
      <td>
<img src="https://user-images.githubusercontent.com/93873940/235385824-fcb8b069-b81e-46c7-9ac0-5cc08da33fe7.png" alt="Screenshot">
      </td>
      <td>
        <img src="https://user-images.githubusercontent.com/93873940/235385986-e4229225-6911-4c76-b469-cdf880b178e7.png" alt="Screenshot">
      </td>
    </tr>
  </tbody>
</table>

## Travelling Courier Problem
To tackle the travelling courier problem, our team explored different ways of implementing iterative improvement to a result generated by a Greedy algorithm

<table>
  <tbody>
    <tr>
      <td>Approaches</td>
      <td>Type</td>
      <td>Results</td>
    </tr>
    <tr>
      <td>Greedy Algorithm</td>
      <td>
        A Greedy Algorithm is simply an algorithm that always considers the closest legal option when doing a pick-up or drop-off. It continues to do so until np legal options are ;eft to explore, meaning all pickups and drop offs are completed.
      </td>
      <td>
     <img src="https://user-images.githubusercontent.com/93873940/235388406-83acad25-2c11-4083-9871-6d52f89d3882.png" alt="Screenshot">   
      </td>
    </tr>
    <tr>
      <td>Greedy++</td>
      <td>
        Greedy++ is a modified version of Greedy where we implement Multi-Start, meaning we consider all possible starting positions of the Courier route. As there are more than 1 depot, we consider all the possible ways to start the path and take the one that generates the lowest travel time.
      </td>
      <td>
        <img src="https://user-images.githubusercontent.com/93873940/235388450-09f007d3-dc79-4811-a4c8-c66d81569693.png" alt="Screenshot">
      </td>
    </tr>
        <tr>
      <td>Swapping</td>
      <td>
Taking the best result from Greedy++, we perform a swap by picking 2 locations,(could be a pick up or drop off). We ensure that the swap is legal and generates a better path. If these conditions are met, we alter tha path and make that the new path. We continue doing so until it no longer makes any improvements to the path.
      </td>
      <td>
      <img src="https://user-images.githubusercontent.com/93873940/235389243-9ea2e081-c098-4f83-a329-a584b6863f2c.png" alt="Screenshot">
      </td>
    </tr>    
    <tr>
      <td>2-opt Reversal</td>
      <td>
Taking the best result from Greedy++, we implemented 2opt by first making 2 cuts in our existing path, take the middle section and flip it, reconnect them. We ensure that the reversal is legal and it improves our QoR scores. This is not as effective as there are a very small portion of possibilities where this pertubation is legal.
      </td>
      <td>
        <img src="https://user-images.githubusercontent.com/93873940/235389505-07c62026-7df1-42e7-8c4e-19422f840d1b.png" alt="Screenshot">
      </td>
    </tr>
    <tr>
      <td>2-opt Shifting + Reversal</td>
      <td>
Taking the best result from Reversal, we take the best path found so far and introduce a shifting pertubation where we make 2 cuts in our existing path, we take the middle section and shift it down by a number of times. We also ensure that the shift is legal and shows improvment before making any changes.
      </td>
      <td>
<img src="https://user-images.githubusercontent.com/93873940/235389682-35fef330-7dff-4005-82a9-391161c56bd5.png" alt="Screenshot">
      </td>
    </tr>
  </tbody>
</table>

