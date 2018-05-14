package org.launchcode.hellospring.Controllers;

import org.apache.catalina.servlet4preview.http.HttpServletRequest;
import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.*;

import javax.xml.ws.RequestWrapper;

//this lets spring know the class should fx as the controller.
@Controller
/**
 * to receive query params. need to respond to greet user by name
 */
public class HelloController {

    /**
     * specifies which route corresponds to this controller
     * you need a @requestmapping for every controller method
     * that needs to responod to a request.
     * value specifies the path to be mapped to controller method
     * allows route of site to be mapped to controller method
     */
    @RequestMapping(value ="")  //this is an empty path segment
    @ResponseBody   //returns as plain text

    //this returns hello world
    /**
     * Action: to receive query params that greet user by name
     * the below allows you to get params passed in via query string
     * HttpServletRequest request - is an obj in method to pass it to handler. gives method the request
     * once reeive, request is an obj that reps data in HTTP request the server receives.
     *
     */
    public String index(HttpServletRequest request) {
        String name = request.getParameter("name");  //this object is added to methods input param. key has to match key in query string " "

        if (name  == null) {
            name = "World";     //if user doesn't pass in a param, they are greeted w/hello world

            return "Hello " + name;
        //when you enter http://localhost:8080/?name=chanda
        //"Hello chanda" returns.

        }
    }

    /**
     * how to handle POST parameters.
     * display form that allows user to submit a request
     * create a new request handler
     */

    @RequestMapping(value ="hello", method = RequestMethod.GET) //method should only reeive requests
    @ResponseBody
    public String helloForm() {
        String html = "<form method ='post'>" +   //if you leave the action param off of form then the form will post to exact url the form is displayed at.
                "<input type='text' name='name' />" +      //action = "someUrl"
                "<input type='submit' value='Greet Me!'/>" +
                "</form>";
        return html;
    }
    //this will live at the same url as above. it should handle post requests
    @RequestMapping(value="hello", method = RequestMethod.POST)

    //to handle requests submitted from the form
    public String helloPost(HttpServletRequest request) { //allows you to get data out of request
        String name = request.getParameter("name"); //key in string has to match key in form

        return "Hello " + name;

    }
    @RequestMapping(value = "hello/{name}") //sets up route request will live name is a param for
    @ResponseBody
    public String helloUrlSegment(@PathVariable String name) { //spring should get value of this param from varibale in the path
        return "Hello " + name;
    }

    //this is accessible by localhost:8080/goodbye
    @RequestMapping(value = "goodbye")
    @ResponseBody
    public String goodbye() {
        return "redirect:/";
    }
}


