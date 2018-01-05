// C function to simulate the cerenkov photons distribution detected by time and radius
// Initial time=1.2*2/3e8=8e-9second=8ns
// Setting the unit of time is nanosecond(ns)
// Setting the unit of radius is millimeter(mm)
// time range(1-25)ns
// radius range(0-900)mm
// f(t)=0.125*cos(42degree)*t is the probability function of detected photon vs time 
// f(r)=((0.104)^2)/((r-0.36)^2+(r-0.72)^2) is the probability function of detected photon vs radius for totally specualr reflection
// spec_prob is the probility of reflections on wall that are specular
//
#include <stdlib.h>
#include <stdio.h>
#include <math.h>
#include "simulation.h"

// To return time & radius distribution together, using pointer
void simulation(double spec_prob, double *time, double *radius)
{
	double r1,r2,r3,t,r,x,y;
	// Check for specular reflection 
	r1 = (double)random()/(double)RAND_MAX;
	if (r1 <= spec_prob)
	{
		//check time
		t = 25.*(double)random()/(double)RAND_MAX;
		x = 0.125*cos(M_PI*42./180.)*t;
		r2 = (double)random()/(double)RAND_MAX;
		if( r2 <= x)
		{
			*time = t;
			return;
		}
		//check radius
		r = 0.9*(double)random()/(double)RAND_MAX;	
		y = pow(0.104,2.)/(pow((r-0.36),2.)+pow((r-0.72),2.));
		r3 = (double)random()/(double)RAND_MAX;
		if( r3 <= y)
		{
			*radius = r;
			return;
		}
	}
	// if not specular, then diffusion, too complicated(angle) to control,out
}
