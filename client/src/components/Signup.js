import { useNavigate } from "react-router-dom";
import React from "react";
import { useFormik } from "formik";
import * as yup from "yup";

function Signup({ updateUser }) {
  const navigate = useNavigate();

  const formSchema = yup.object().shape({
    name: yup.string().required("Please enter a name"),
    username: yup.string().required("Please enter a username"),
    img: yup.string().required("Please enter an image"),
    password: yup.string().required("Please enter a password"),
  });
  const formik = useFormik({
    initialValues: {
      username: "",
      name: "",
      img: "",
      password: "",
    },
    validationSchema: formSchema,
    onSubmit: (values, actions) => {
      fetch(
        "http://127.0.0.1:5555/signup",

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
        }
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
            id="name"
            className="form-control"
            type="text"
            name="name"
            onChange={formik.handleChange}
            onBlur={formik.handleBlur}
            value={formik.values.name}
            placeholder="Add name here"
          ></input>
          {formik.touched.name && formik.errors.name ? (
            <h6 style={{ color: "red" }}>{formik.errors.name}</h6>
          ) : (
            ""
          )}
          <label className="form-label" htmlFor="name">
            Name
          </label>
        </div>

        <div className="form-floating" style={{ marginBottom: "10px" }}>
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
            id="img"
            className="form-control"
            type="text"
            name="img"
            onChange={formik.handleChange}
            value={formik.values.img}
            onBlur={formik.handleBlur}
            placeholder="Image here"
          />
          {formik.touched.img && formik.errors.img ? (
            <h6 style={{ color: "red" }}>{formik.errors.img}</h6>
          ) : (
            ""
          )}

          <label className="form-label" htmlFor="img">
            Image
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
          value="signup"
        ></input>
      </form>
    </div>
  );
}

export default Signup;
