import Plyr from 'plyr'
import 'plyr/dist/plyr.css'

import { ready } from '../../utils'

ready(() => {
  const player = new Plyr('#video-player', {
    ratio: '16:9',
    autoplay: true,
    keyboard: {focused: false, global: false},
    speed: {
      selected: 1,
      options: [0.5, 0.75, 1]
    }
  })
})
