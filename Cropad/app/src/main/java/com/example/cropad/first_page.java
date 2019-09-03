package com.example.cropad;

import androidx.appcompat.app.AppCompatActivity;

import android.content.Intent;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.ImageView;
import android.widget.ViewFlipper;

public class first_page extends AppCompatActivity {

    public Button log_out;
    ViewFlipper v_flip;

    public Button add_market;
    public Button weather;

    public void flipperimage(int image){
        ImageView imgview =new ImageView(this);
        imgview.setBackgroundResource(image);
        v_flip.addView(imgview);
        v_flip.setFlipInterval(4000);
        v_flip.setAutoStart(true);

        v_flip.setInAnimation(this,android.R.anim.slide_in_left);
        v_flip.setOutAnimation(this,android.R.anim.slide_out_right);
    }

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_first_page);

        int images[] = {R.drawable.logo, R.drawable.weather};
        v_flip = findViewById(R.id.flipper);

        for (int i = 0; i < images.length; i++)
        {
            flipperimage(images[i]);
        }




        log_out= (Button) findViewById(R.id.logout_but);
        log_out.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                Intent l = new Intent(first_page.this, MainActivity.class);
                startActivity(l);
            }
        });

        add_market = (Button) findViewById(R.id.add_market_but);
        add_market.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                Intent addmkt = new Intent(first_page.this, add_market.class);
                startActivity(addmkt);
            }
        });
        weather = (Button) findViewById(R.id.weather);
        weather.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                Intent weather_i = new Intent( first_page.this , weather_forecast.class);
                startActivity(weather_i);
            }
        });
    }
}
