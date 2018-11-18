import { NbMenuItem } from '@nebular/theme';

export const MENU_ITEMS: NbMenuItem[] = [
  {
    title: 'Dashboard',
    icon: 'nb-keypad',
    link: '/pages/dashboard',
    home: true,
  },
  {
    title: 'Upload',
    icon: 'nb-compose',
    children: [
      // {
      //   title: 'Form Inputs',
      //   link: '/pages/forms/inputs',
      // },
      {
        title: 'Datasets',
        link: '/pages/forms/layouts',
      },
    ],
  },
  {
    title: 'Maps',
    icon: 'nb-location',
    children: [
      // {
      //   title: 'Google Maps',
      //   link: '/pages/maps/gmaps',
      // },
      // {
      //   title: 'Leaflet Maps',
      //   link: '/pages/maps/leaflet',
      // },
      {
        title: 'Heat Maps',
        link: '/pages/maps/bubble',
      },
      {
        title: 'Location Maps',
        link: '/pages/maps/searchmap',
      },
    ],
  },
];
