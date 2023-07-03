import { useNavigate, Link } from "react-router-dom";
import React from "react";
import { useFormik } from "formik";
import * as yup from "yup";

function Login({ updateUser, user }) {
  const navigate = useNavigate();

  const formSchema = yup.object().shape({
    username: yup.string().required("Please enter a username"),
    password: yup.string().required("Please enter a password"),
  });
  const formik = useFormik({
    initialValues: {
      username: "",
      password: "",
    },
    validationSchema: formSchema,
    onSubmit: (values, actions) => {
      fetch("http://127.0.0.1:5555/login", {
        method: "POST",
        headers: {
          "content-type": "application/json",
        },
        body: JSON.stringify(values),
      }).then((res) => {
        res.json().then((data) => {
          updateUser(data);
          actions.resetForm();
          navigate("/");
        });
      });
    },
  });

  return (
    <div className="container">
      <form onSubmit={formik.handleSubmit} className="form">
        <div
          className="form-floating"
          style={{ marginBottom: "10px", marginTop: "40px" }}
        >
          <input
            id="username"
            className="form-control"
            type="text"
            name="username"
            onChange={formik.handleChange}
            value={formik.values.username}
            onBlur={formik.handleBlur}
            placeholder="Username here"
          ></input>
          {formik.touched.username && formik.errors.username ? (
            <h6 style={{ color: "red" }}>{formik.errors.username}</h6>
          ) : (
            ""
          )}
          <label className="form-label" htmlFor="username">
            Username
          </label>
        </div>

        <div className="form-floating" style={{ marginBottom: "10px" }}>
          <input
            id="password"
            className="form-control"
            type="password"
            name="password"
            onChange={formik.handleChange}
            value={formik.values.password}
            onBlur={formik.handleBlur}
            placeholder="password here"
          ></input>
          {formik.touched.password && formik.errors.password ? (
            <h6 style={{ color: "red" }}>{formik.errors.password}</h6>
          ) : (
            ""
          )}

          <label className="form-label" htmlFor="password">
            Password
          </label>
        </div>
        <input
          className="btn btn-primary"
          style={{ width: "100%" }}
          type="submit"
          value="Login"
        ></input>
      </form>
      <button style={{ marginTop: "40px" }} className="btn btn-warning">
        <Link style={{ textDecoration: "none", color: "black" }} to={"/signup"}>
          Don't have an account yet?
          <br /> Signup here
        </Link>
      </button>
    </div>
  );
}

export default Login;
