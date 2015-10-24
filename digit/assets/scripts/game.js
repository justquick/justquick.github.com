(function() {
  var Mario, choose,
    __bind = function(fn, me){ return function(){ return fn.apply(me, arguments); }; };

  choose = function(choices) {
    return choices[Math.floor(Math.random() * choices.length)];
  };

  Mario = (function() {
    function Mario() {
      this.update = __bind(this.update, this);
      this.create = __bind(this.create, this);
      this.preload = __bind(this.preload, this);
      this.createBaddie = __bind(this.createBaddie, this);
      this.gameOver = __bind(this.gameOver, this);
      this.collectStar = __bind(this.collectStar, this);
      this.game = new Phaser.Game(800, 600, Phaser.AUTO, '', {
        preload: this.preload,
        create: this.create,
        update: this.update
      });
      this.score = 0;
      this.scoreText;
    }

    Mario.prototype.collectStar = function(player, star) {
      star.kill();
      this.score += 1;
      this.scoreText.text = 'Score: ' + this.score;
      if (this.score === 13) {
        this.scoreText.text = 'YOU WIN!';
        return this.game.paused = true;
      }
    };

    Mario.prototype.gameOver = function(player, baddie) {
      this.scoreText.text = 'GAME OVER!';
      return this.game.paused = true;
    };

    Mario.prototype.createBaddie = function() {
      var baddie;
      baddie = this.game.add.sprite(Math.random() * 800, 0, 'baddie');
      this.game.physics.arcade.enable(baddie);
      baddie.body.bounce.y = 0.0;
      baddie.body.gravity.y = 10000;
      baddie.body.collideWorldBounds = true;
      baddie.animations.add('left', [0, 1], 10, true);
      baddie.animations.add('right', [2, 3], 10, true);
      baddie.direction = choose(['left', 'right']);
      return this.baddies.push(baddie);
    };

    Mario.prototype.preload = function() {
      this.game.load.image('sky', 'assets/images/sky.png');
      this.game.load.image('grass', 'assets/images/grass.png');
      this.game.load.image('star', 'assets/images/star.png');
      this.game.load.image('rock', 'assets/images/rock.png');
      this.game.load.spritesheet('dude', 'assets/images/dude.png', 32, 48);
      this.game.load.spritesheet('baddie', 'assets/images/baddie.png', 32, 32);
      return this.cursors = this.game.input.keyboard.createCursorKeys();
    };

    Mario.prototype.create = function() {
      var h, i, rock, star, tile, w, _i, _j, _k;
      this.game.add.sprite(0, 0, 'sky');
      this.scoreText = this.game.add.text(16, 16, 'Score: 0', {
        fontSize: '32px',
        fill: '#000'
      });
      this.platforms = window.platforms = this.game.add.group();
      this.platforms.enableBody = true;
      this.tiles = window.tiles = {};
      this.baddies = window.baddies = [];
      for (w = _i = 0; _i <= 16; w = ++_i) {
        for (h = _j = 1; _j <= 10; h = ++_j) {
          tile = this.platforms.create(w * 50, h * 50, 'grass');
          tile.body.immovable = true;
          tile.body.checkCollision.left = false;
          tile.body.checkCollision.down = false;
          tile.body.checkCollision.right = false;
          if (this.tiles[w] == null) {
            this.tiles[w] = {};
          }
          this.tiles[w][h] = tile;
        }
        rock = this.platforms.create(w * 50, 550, 'rock');
        rock.body.immovable = true;
      }
      this.player = window.player = this.game.add.sprite(0, 0, 'dude');
      this.game.physics.arcade.enable(this.player);
      this.player.body.bounce.y = 0.2;
      this.player.body.gravity.y = 600;
      this.player.body.collideWorldBounds = true;
      this.player.animations.add('left', [0, 1, 2, 3], 10, true);
      this.player.animations.add('right', [5, 6, 7, 8], 10, true);
      this.stars = this.game.add.group();
      this.stars.enableBody = true;
      for (i = _k = 0; _k <= 12; i = ++_k) {
        star = this.stars.create(Math.random() * 800, Math.random() * 550, 'star');
        star.body.gravity.y = 600;
        star.body.bounce.y = 0.7 + Math.random() * 0.2;
      }
      return this.game.time.events.repeat(Phaser.Timer.SECOND * 3, 10, this.createBaddie);
    };

    Mario.prototype.update = function() {
      var algo, baddie, tile, x, y, _i, _j, _k, _len, _len1, _len2, _ref, _ref1, _ref2, _results;
      this.game.physics.arcade.collide(this.player, this.platforms);
      this.game.physics.arcade.collide(this.baddie, this.platforms);
      this.game.physics.arcade.collide(this.platforms, this.stars);
      this.game.physics.arcade.overlap(this.player, this.stars, this.collectStar);
      this.player.body.velocity.x = 0;
      _ref = this.baddies;
      for (_i = 0, _len = _ref.length; _i < _len; _i++) {
        baddie = _ref[_i];
        this.game.physics.arcade.collide(baddie, this.platforms);
        if (baddie.body.position.x === 0) {
          baddie.direction = 'right';
        } else if (baddie.body.position.x === 768) {
          baddie.direction = 'left';
        }
        if (baddie.direction === 'right') {
          baddie.body.velocity.x = 300;
          baddie.animations.play('right');
        } else {
          baddie.body.velocity.x = -300;
          baddie.animations.play('left');
        }
      }
      if (this.cursors.left.isDown) {
        this.player.body.velocity.x = -150;
        this.player.animations.play('left');
      } else if (this.cursors.right.isDown) {
        this.player.body.velocity.x = 150;
        this.player.animations.play('right');
      } else {
        this.player.animations.stop();
        this.player.frame = 4;
      }
      if (this.cursors.up.isDown && this.player.body.touching.down) {
        this.player.body.velocity.y = -350;
      }
      if (this.cursors.down.isDown && this.player.body.touching.down) {
        x = this.player.position.x / 50;
        y = this.player.position.y / 50 + 1;
        _ref1 = [Math.round, Math.floor, Math.ceil];
        for (_j = 0, _len1 = _ref1.length; _j < _len1; _j++) {
          algo = _ref1[_j];
          tile = this.tiles[algo(x)][algo(y)];
          if ((tile != null) && tile.visible) {
            tile.destroy();
            tile.body.checkCollision.up = false;
            break;
          }
        }
        this.player.body.velocity.y = 50;
      }
      this.game.physics.arcade.collide(this.player, this.platforms);
      _ref2 = this.baddies;
      _results = [];
      for (_k = 0, _len2 = _ref2.length; _k < _len2; _k++) {
        baddie = _ref2[_k];
        _results.push(this.game.physics.arcade.collide(this.player, baddie, this.gameOver));
      }
      return _results;
    };

    return Mario;

  })();

  window.mario = new Mario;

}).call(this);
