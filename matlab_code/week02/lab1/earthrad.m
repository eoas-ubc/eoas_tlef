% Script to calculate the surface area of the Earth in cubic km

%%
radius=6371;
area=pi*radius*radius

%% Calculating radii that are 5km bigger, 20.3km smaller and 25% of Earth's
% radius
rad2=radius+5
rad3=radius-20.3
rad4=0.25*radius