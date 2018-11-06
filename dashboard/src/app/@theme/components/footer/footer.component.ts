import { Component } from '@angular/core';

@Component({
  selector: 'ngx-footer',
  styleUrls: ['./footer.component.scss'],
  template: `
    <span class="created-by">Created with ♥ by <b><a href="https://amfoss.in" target="_blank">amfoss</a></b>
     inspired by <b><a href="https://akveo.com" target="_blank">akveo</a></b> 2017</span>
    <div class="socials">
      <a href="https://github.com/amfoss/" target="_blank" class="ion ion-social-github"></a>
      <a href="https://www.facebook.com/amfoss.in/" target="_blank" class="ion ion-social-facebook"></a>
      <a href="https://twitter.com/amfoss_in" target="_blank" class="ion ion-social-twitter"></a>
      <a href="https://www.instagram.com/amfoss.in/" target="_blank" class="ion ion-social-instagram"></a>
    </div>
  `,
})
export class FooterComponent {
}
