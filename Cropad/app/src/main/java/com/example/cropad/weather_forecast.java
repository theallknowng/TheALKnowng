package com.example.cropad;

import androidx.appcompat.app.AppCompatActivity;

import android.os.Bundle;
import android.widget.TextView;
import android.widget.Toast;

import com.android.volley.RequestQueue;
import com.android.volley.VolleyError;
import com.android.volley.toolbox.Volley;

import org.json.JSONException;
import org.json.JSONObject;
import java.text.SimpleDateFormat;
import java.util.Date;

public class weather_forecast extends AppCompatActivity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_weather_forecast);

        TextView datecurrent = findViewById(R.id.datetime);
        SimpleDateFormat sdf =  new SimpleDateFormat("yyyy.MM.dd ");
        String currentdate = sdf.format(new Date());
        datecurrent.setText(currentdate);

        String url="http://10.0.4.196:5656/user/login";
        RequestQueue requestQueue = Volley.newRequestQueue(weather_forecast.this);
        JSONObject jsonObject = new JSONObject();

//        final String requestBody = jsonObject.toString();
//        ConnectionManager.sendData(requestBody, requestQueue, url, new ConnectionManager.VolleyCallback() {
//            @Override
//            public void onSuccessResponse(String result) {
//
//                JSONObject jsonObject= null;
//                try {
//                    jsonObject = new JSONObject(result);
//                } catch (JSONException e) {
//                    e.printStackTrace();
//                }
//
//                String success= null;
//                try {
//                    success = jsonObject.getString("success");
//                } catch (JSONException e) {
//                    e.printStackTrace();
//                }
//
//                if(success.equals("true")){
//                    firstpag();
//                }
//                else
//                {
//                    Toast.makeText(weather_forecast.this,"Invalid Credentials",Toast.LENGTH_SHORT).show();
//                }
//            }
//
//            @Override
//            public void onErrorResponse(VolleyError error) {
//                Toast toast = Toast.makeText(MainActivity.this,"Could not log in "+error,Toast.LENGTH_LONG);
//                toast.show();
//            }
//        });
    }
}
