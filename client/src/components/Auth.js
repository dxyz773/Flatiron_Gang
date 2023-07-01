import { useNavigate } from "react-router-dom";
import React, { useState } from "react";
import { useFormik } from "formik";
import * as yup from "yup";

function Auth({ updateUser }) {
  const [signup, setSignup] = useState(false);
  // 8a. create state error

  const navigate = useNavigate();
  const toggleSignup = () => setSignup((prev) => !prev);

  const formSchema = yup.object().shape({
    name: yup.string(),
    username: yup.string().required("Please enter a username"),
    img: yup.string().required("Please enter an image"),
    password: yup.string().required("Please enter a password"),
  });
  const formik = useFormik({
    initialValues: {
      username: "",
      img: "",
      name: "",
      password: "",
    },
    validationSchema: formSchema,
    onSubmit: (values, actions) => {
      fetch(
        signup ? "http://127.0.0.1:5555/signup" : "http://127.0.0.1:5555/login",
        {
          method: "POST",
          headers: {
            "content-type": "application/json",
          },
          body: JSON.stringify(values),
        }
      ).then((res) => {
        if (res.ok) {
          res.json().then((data) => {
            actions.resetForm();
            updateUser(data);
            navigate("/");
          });
        } else {
          // 8b. set error message
        }
      });
    },
  });

  return (
    <section>
      {signup ? (
        <form className="form" onSubmit={formik.handleSubmit}>
          <label>Name</label>
          <input
            type="text"
            name="name"
            value={formik.values.name}
            onChange={formik.handleChange}
            onBlur={formik.handleBlur}
          />
          <label>Username</label>
          <input
            type="text"
            name="username"
            value={formik.values.username}
            onChange={formik.handleChange}
            onBlur={formik.handleBlur}
          />
          {/* formik.touched is enabled with onBlur */}
          {/*
						1. onBlur events - toggles formik.touched
						2. conditional: if formik.touched and formik.errors
					*/}
          {formik.touched.username && formik.errors.username ? (
            <h3>{formik.errors.username}</h3>
          ) : (
            ""
          )}
          <label>Image</label>
          <input
            type="text"
            name="img"
            value={formik.values.img}
            onChange={formik.handleChange}
            onBlur={formik.handleBlur}
          />
          {/* formik.touched is enabled with onBlur */}
          {/*
						1. onBlur events - toggles formik.touched
						2. conditional: if formik.touched and formik.errors
					*/}
          {formik.touched.img && formik.errors.img ? (
            <h3>{formik.errors.img}</h3>
          ) : (
            ""
          )}
          <label>Password</label>

          <input
            type="password"
            name="password"
            value={formik.values.password}
            onChange={formik.handleChange}
            onBlur={formik.handleBlur}
          />
          {formik.touched.password && formik.errors.password ? (
            <h3>{formik.errors.password}</h3>
          ) : (
            ""
          )}
          <input type="submit" value="Signup" className="button" />
          {/* 8c. use conditional rendering to display the error to user */}
        </form>
      ) : (
        <form className="form" onSubmit={formik.handleSubmit}>
          <label>Username</label>

          <input
            type="text"
            name="username"
            value={formik.values.username}
            onChange={formik.handleChange}
            onBlur={formik.handleBlur}
          />
          {formik.touched.username && formik.errors.username ? (
            <h3>{formik.errors.username}</h3>
          ) : (
            ""
          )}
          <label>Password</label>

          <input
            type="password"
            name="password"
            value={formik.values.password}
            onChange={formik.handleChange}
            onBlur={formik.handleBlur}
          />
          {formik.touched.password && formik.errors.password ? (
            <h3>{formik.errors.password}</h3>
          ) : (
            ""
          )}
          <input type="submit" value="Login" className="button" />
          {/* 8c. use conditional rendering to display the error to user */}
        </form>
      )}
      <section>
        <p>{signup ? "Already have an account?" : "Not a member?"}</p>
        <button className="button" onClick={toggleSignup}>
          {signup ? "Login" : "Sign Up"}
        </button>
      </section>
    </section>
  );
}

export default Auth;
